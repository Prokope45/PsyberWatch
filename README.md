# PsyberWatch
A Kansas State University STAT-766 project involving the multi-classification of legitimate, unsolicited, and harmful emails for cybersecurity purposes.

## Quick Setup
This setup assumes that your Python executable is on PATH.

1. Create local virtual environment `python3 -m venv .venv`.
2. Activate virtual environment `source .venv/bin/activate`.
3. Install dependencies `pip install -r requirements.txt`.
4. Access jupyter notebooks and inspect cells.

## Ham, Spam, or Phish?

### Problem Statement
People are inundated with emails being sent to them on a daily, if not, hourly basis. A lot of emails may be legitimate, or illegitimate and/or dangerous due to risks of scams and bad actors attempting to gain access to the user's account. Existing systems in place are efficient in detecting spam, but AI-enhanced phishing emails are enabling threat actors to enhance their attacks by generating message that look and read like legitimate mail.

### Project Proposal
This project aims to build a supervised machine learning model that is trained on ham (wanted mail), spam (unwanted mail), and phishing (dangerous mail) emails. Once the model is trained and tested, it will be connected to a Microsoft Outlook account via API to read emails at a fixed interval (~5 minutes), analyze the emails, and text the user about a potentially risky email that could be a phishing attack. Full end-to-end testing will involve creating fake emails that imitate institutions/people and using an LLM to generate a realistic email message.

### Technologies Used
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
