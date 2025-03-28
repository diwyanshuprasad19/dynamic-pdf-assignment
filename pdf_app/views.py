import os
import hashlib
from django.http import FileResponse, JsonResponse
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework import status
from weasyprint import HTML
from django.conf import settings

class GeneratePDFView(APIView):

    def post(self, request):
        data = request.data
        # Generate a unique hash for the data
        data_hash = hashlib.md5(str(data).encode('utf-8')).hexdigest()
        pdf_file_name = f"{data_hash}.pdf"
        pdf_file_path = os.path.join(settings.MEDIA_ROOT, pdf_file_name)
        
        # Check if the file already exists
        if os.path.exists(pdf_file_path):
            return FileResponse(open(pdf_file_path, 'rb'), content_type='application/pdf')

        # Render HTML with the received data
        html_string = render_to_string('pdf_app/invoice_template.html', {'data': data})
        html = HTML(string=html_string)
        html.write_pdf(target=pdf_file_path)

        return FileResponse(open(pdf_file_path, 'rb'), content_type='application/pdf')
