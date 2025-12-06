# PsyberWatch
A Kansas State University STAT-766 project involving the multi-classification of legitimate, unsolicited, and harmful emails for cybersecurity purposes.

---

## Ham, Spam, or Phish?

### Problem Statement
People are inundated with emails being sent to them on a daily, if not, hourly basis. A lot of emails may be legitimate, or illegitimate and/or dangerous due to risks of scams and bad actors attempting to gain access to the user's account. Existing systems in place are efficient in detecting spam, but AI-enhanced phishing emails are enabling threat actors to enhance their attacks by generating message that look and read like legitimate mail.

### Project Proposal
This project aims to build a supervised machine learning model that is trained on ham (wanted mail), spam (unwanted mail), and phishing (dangerous mail) emails. Once the model is trained and tested, it will be integrated into a webapp that allows users to paste in suspecious text into the text box to see if it is a legitimate or potentially dangerous email. After end-to-end testing is complete, the webapp will be deployed on Digital Ocean or an equivalent cloud provider to allow users to access from anywhere in the world.

### Future Features
- Allow for external mailboxes, like Thunderbird or Outlook or GMail to be connected to webapp via API or other means so that emails may be forwarded or retrieved for analysis.
- Upon completion of mailbox integration, the webapp can run an email body analysis and send a text message if it detects a phishing email. This process would be executed at a fixed interval using a web worker, such as a Celery task.
- Add training of LLM-enhanced phishing emails as a separate category (to be referred to as "imitations") where imitated emails look and read very well like ham emails due to the capability of LLMs imitating human speech that can be indistinguishable to actual human speech unless carefully examined.

---

## Configuration & and Setup Diagnosis

### Quick Setup
This setup assumes that your Python executable is on PATH.

### Setup with PIP environment
1. Create local virtual environment `python3 -m venv .svm-venv`.
2. Activate virtual environment `source .svm-venv/bin/activate`.
3. Install dependencies `pip install -r requirements.txt`.
4. Access jupyter notebooks and inspect cells.

### Setup with Conda environment
1. Create local virtual environment `conda env create svm-venv -f environment.yml`. Accept or decline any prompts shown during configuration.
2. Activate virtual environment `conda activate svm-venv`.
3. Access jupyter notebooks and inspect cells.

#### Running project in Jupyter Notebooks
If you wish to run the project in Jupyter Notebooks, please ensure that [jupyter](https://jupyter.org/install) is installed on your system. If you are on Windows but want to run Unix/Linux commands, install [wsl](https://learn.microsoft.com/en-us/windows/wsl/install) or Windows Subsystem for Linux, which allows you to run a Linux distribution within Windows.

Once Jupyter Notebooks has been installed, activate `svm-env` (conda or pip) and run:
`conda install ipykernel` or `pip3 install ipykernel`

then

```
python -m ipykernel install --user --name=svm-venv --display-name "Python svm-venv"
```

or

```
python -m ipykernel install --user --name=.svm-venv --display-name "Python .svm-venv"
```

This will allow you to use the `svm-venv` environment within Jupyter Notebooks as a selectable Kernel.

---


### Problems that may Arise During Setup

When loading `sentence-transformers`, this error may be raised: `ModuleNotFoundError: Could not import module 'PreTrainedModel'. Are this object's requirements defined correctly?`. This is not an issue with the environment, but rather with a version incompatibility between:

```
sentence-transformers     5.1.2
transformers              4.57.3
```

The fix is to pin both packages to previous compatible versions:

```
pip3 uninstall sentence-transformers transformers
pip3 install sentence-transformers==3.0.1 transormers==4.35.2
```

To keep `sentence-transformers` at the latest version, you may also try `transormers==4.35.2` with `sentence-transformers==4.1.0`.

---

## Technologies Used
- [Support Vector Machine (SVM) One-vs-One Model](https://www.geeksforgeeks.org/machine-learning/multi-class-classification-using-support-vector-machines-svm/)
	- Classifier votes one each pairing of a small set of classes for the best fit of the target variable.
	- Grouping formed as (Ham vs Spam), (Ham vs Phish), and (Spam vs Phish)
- Microsoft Outlook API (to create account).
- Python (backend processing using machine learning packages and numpy/pandas)
- Python (frontend, to run server and periodically call API to read emails)

https://learn.microsoft.com/en-us/outlook/rest/get-started

https://zyrog.medium.com/building-an-ai-powered-email-classifier-detecting-ham-spam-and-phishing-12dadd17f323

https://www.vonage.com/communications-apis/sms/

https://www.geeksforgeeks.org/python/send-an-sms-message-with-python/

https://www.geeksforgeeks.org/machine-learning/multi-class-classification-using-support-vector-machines-svm/

https://www.geeksforgeeks.org/machine-learning/support-vector-machine-algorithm/
