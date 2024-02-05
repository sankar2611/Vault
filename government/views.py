from django.shortcuts import render

# Create your views here.

def gov(request):
    return render(request, 'government/gov.html')

def document(request):
    return render(request, 'government/document.html')