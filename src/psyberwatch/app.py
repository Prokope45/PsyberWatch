import threading
import time
import panel as pn
import pandas as pd
import joblib
from src.psyberwatch.utils import clean_text
from src.model_logging.logging_config import logger


sbert = joblib.load("./models/sbert.joblib")
svm = joblib.load("./models/svm_model.joblib")

pn.extension(notifications=True)   # enable notification system

#######################################################
# 1. Theme / Styling
#######################################################

custom_css = """
body, .bk {
    background-color: #ffffff !important;
}

.bk-btn-primary {
    background-color: #6a0dad !important;
    border-color: #6a0dad !important;
    color: white !important;
}

.bk-btn-primary.bk-btn-default[disabled] {
    opacity: 0.6 !important;
}

.bk-btn-secondary {
    background-color: #808080 !important;
    border-color: #808080 !important;
    color: white !important;
}

.bk-panel-model {
    background-color: white !important;
}

.title-text {
    font-size: 36px;
    font-weight: bold;
    color: #6a0dad;
    text-align: center;
}

.subtitle-text {
    font-size: 16px;
    color: #333333;
    text-align: center;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

/* Make spinner purple */
.bk-loading-spinner .bk-spinner > div {
    background-color: #6a0dad !important;
}
"""

pn.config.raw_css.append(custom_css)

#######################################################
# 2. Model + Mapping
#######################################################

email_dataframe = pd.read_feather("./data/2_clean_email_dataset.feather")

mapping = dict(zip(
    email_dataframe["Email Type"].astype("category").cat.codes.unique(),
    email_dataframe["Email Type"].unique()
))

def encode_email(email_text):
    cleaned = clean_text(email_text)
    embedding = sbert.encode(
        cleaned,
        convert_to_numpy=True
    ).reshape(1, -1)
    return embedding

def classify_email(email_text):
    embedding = encode_email(email_text)
    prediction = svm.predict(embedding)[0]
    return mapping[prediction]

#######################################################
# 3. Panel Widgets
#######################################################

title = pn.pane.Markdown(
    "<div class='title-text'>STAT 766 - Email Classifier</div>",
)

subtitle = pn.pane.Markdown(
    """
This tool is part of the STAT 766 project on supervised machine learning 
for classifying email messages into **Ham**, **Spam**, or **Phishing** categories.  
Paste any email text below and click **Classify** to see the model’s prediction.
""",
    css_classes=["subtitle-text"]
)

email_text = pn.widgets.TextAreaInput(
    name="Email Contents",
    placeholder="Drop email text contents here",
    height=200,
    width=700
)

classify_button = pn.widgets.Button(
    name="Classify",
    button_type="primary",
    width=200
)

result_display = pn.pane.Markdown("", width=700)

#######################################################
# 4. Callback with Error Handling + Loading State
#######################################################

spinner_chars = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']

def on_classify(event):
    text = email_text.value.strip()
    if not text:
        result_display.object = "⚠️ **Please enter email text first.**"
        return

    classify_button.disabled = True
    result_display.object = ""
    spinner_index = 0

    # This function will be called periodically by Panel
    def spinner_tick():
        nonlocal spinner_index
        classify_button.name = f"{spinner_chars[spinner_index % len(spinner_chars)]} Classifying..."
        spinner_index += 1

    # Register periodic callback; Panel starts it automatically
    callback = pn.state.add_periodic_callback(spinner_tick, 100)

    def run_classification():
        time.sleep(3)  # artificial delay

        try:
            label = classify_email(text)
            result_display.object = f"### 📧 Classification Result: **{label}**"
        except Exception as e:
            pn.state.notifications.error(f"An error occurred: {e}", duration=6000)
            result_display.object = "❌ **Classification failed. See notification above.**"
        finally:
            # Stop spinner
            callback.stop()
            classify_button.disabled = False
            classify_button.name = "Classify"

    threading.Thread(target=run_classification).start()

classify_button.on_click(on_classify)

#######################################################
# 5. Layout
#######################################################

layout = pn.Column(
    pn.Spacer(height=50),
    pn.Column(
        title,
        subtitle,
        pn.Spacer(height=20),
        email_text,
        pn.Spacer(height=10),
        pn.Row(classify_button, align="center"),
        pn.Spacer(height=20),
        result_display,
        align="center",
        sizing_mode="fixed",
    ),
    align="center",
    sizing_mode="stretch_width",
)

result_display.css_classes = ["result-display"]
custom_result_css = """
.result-display {
    font-size: 24px;
    font-weight: bold;
    color: #6a0dad;  /* purple */
    text-align: center;
}
"""
pn.config.raw_css.append(custom_result_css)

layout.servable()
