# Dynamic PDF Generation Service (Django)

This Django-based application provides a REST API to generate PDF documents using **WeasyPrint**.  
The generated PDFs are stored in local storage, and if the same data is provided again, the existing PDF is returned instead of generating it again.  

---

## 📌 Features
- Generate PDF files dynamically based on provided JSON data.
- Save generated PDFs to local storage (`media/` folder).
- Reuse previously generated PDFs if the same data is submitted (caching mechanism).
- REST API that accepts JSON input and returns a downloadable PDF file.
- Well-structured code with separation of views, templates, services, and URL configurations.

---

## 🔍 Requirements
- Python (Version 3.12+)
- Django
- Django REST Framework
- WeasyPrint
- python-dotenv

---

## 🔥 Setup Instructions

### Step 1: Clone the Repository

- git clone <repository-url>
- cd pdf_service
- 

## Create & Activate Virtual Environment

- python -m venv env
- source env/bin/activate  # Linux / Mac
- .\env\Scripts\activate    # Windows

## Install Dependencies

- pip install -r requirements.txt

## Configure Environment Variables (.env)

- Create a .env file in the root directory:

- SECRET_KEY=django-insecure-49fd85e6c92f4bdeb827a88c68e634b9ec37d5c9277e13bfa1b4bffb90d1e8bc

## Create media/ Directory

- mkdir media

## Apply Migrations & Run Server

- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

📊 API Endpoint

- Generate PDF (POST Request)
- URL: http://127.0.0.1:8000/api/v1/generate-pdf/

Method: POST

Headers: Content-Type: application/json

Body (Example):

{
    "seller": "XYZ Pvt. Ltd.",
    "sellerGstin": "29AABBCCDD121ZD",
    "sellerAddress": "New Delhi, India",
    "buyer": "Vedant Computers",
    "buyerGstin": "29AABBCCDD131ZD",
    "buyerAddress": "New Delhi, India",
    "items": [
        {
            "name": "Product 1",
            "quantity": "12 Nos",
            "rate": 123.00,
            "amount": 1476.00
        }
    ]
}

📥 Expected Response (If PDF is Generated)

- The PDF will be returned directly as a downloadable file.

- The file will also be stored in the media/ directory with a unique name based on the input data hash.

📥 Example File Path (Stored Locally)

pdf_service/media/873d2eb09d02b41f1747d037c233141f.pdf

✅ Reusing Generated PDFs
If the same data is provided again, the API will return the previously generated PDF instead of creating a new one.

📦 Dependencies (requirements.txt)

- django
- djangorestframework
- weasyprint
- python-dotenv


📌 Code Explanation

- View (pdf_app/views.py)
- GeneratePDFView: Handles POST requests, generates PDF files, and returns them.

- Saves PDFs in the media/ directory and reuses files if the same data is provided.

🔍 Testing
- To test the API, use Postman or cURL to send a POST request to:

- http://127.0.0.1:8000/api/v1/generate-pdf/
