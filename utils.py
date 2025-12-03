import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def clean_text(text):
    # 1. Lowercase
    text = text.lower()

    # 2. Remove URLs
    text = re.sub(r"http[s]?://\S+|www\.\S+", " ", text)

    # 3. Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # 4. Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # 5. Tokenize
    tokens = word_tokenize(text)

    # 6. Remove stop words + non-alpha words
    tokens = [w for w in tokens if w.isalpha() and w not in stop_words]

    # 7. Lemmatize (optional but improves SVM performance)
    tokens = [lemmatizer.lemmatize(w) for w in tokens]

    return " ".join(tokens)
