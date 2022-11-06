from django.shortcuts import render  
from django.http import HttpResponse  
from mysite.functions import extract_text_from_pdf,extract_emails,extract_phone_number,extract_names
import PyPDF2

from mysite.forms import StudentForm,Form2
from django.core.files.storage import default_storage
def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid(): 
            file = request.FILES['file']
            file_name = default_storage.save(file.name, file)

            #filename = request.FILES['file'].name
            pdfFileObj = open(file_name, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            pageObj = pdfReader.getPage(0)
            text = (pageObj.extractText())
            
            pno = extract_phone_number(text)
            email = extract_emails(text)
            name = extract_names(text)
            return render(request,"form2.html",{'pno':pno,'email':email,'name':name})  
    else:  
        student = StudentForm()  
        return render(request,"index.html",{'form':student})  
   