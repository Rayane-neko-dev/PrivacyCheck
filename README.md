# PrivacyCheck - Web App

## Overview
PrivacyCheck is a Django-based web application designed to **simulate a GDPR compliance evaluation** for a website.  
Users answer a **short questionnaire** regarding data collection, consent, cookies, and privacy policies. The application provides a **compliance score**, explanations, and recommendations for improvement.  

The purpose of this app is **educational** — it demonstrates the intersection of **informatics, legal regulations, and societal impact** of data handling.  

---

## Features
- User-friendly **web form** for answering GDPR-related questions  
- Automatic **evaluation of compliance** (Compliant / Partially Compliant / Non-Compliant)  
- **Explanations and suggestions** for improving privacy practices  
- Simple **dashboard** for displaying results  
- Responsive layout using HTML/CSS (Bootstrap or a free template)  

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/privacycheck.git
cd privacycheck
Create a virtual environment

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Run the development server

python manage.py runserver


Open in browser

http://127.0.0.1:8000/

Project Structure
privacycheck/
├── core/
│   ├── models.py       # Evaluation, Question, Answer models
│   ├── views.py        # Logic for handling forms and results
│   ├── forms.py        # Django forms for questionnaire
│   ├── templates/      # HTML templates
│   └── urls.py         # App-level routes
├── privacycheck/
│   └── settings.py     # Django project settings
├── manage.py
└── requirements.txt

How it works

The user visits the homepage and starts the GDPR questionnaire.

The user answers questions such as:

Does the site collect personal data?

Is there a privacy policy?

Is user consent required?

Are cookies or third-party services used?

The app calculates a compliance level based on the answers.

Results are displayed with:

Compliance rating

List of potential issues

Educational recommendations

Dependencies

Python 3.10+

Django 4.x

Bootstrap 5
