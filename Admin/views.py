from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Admin/home.html')

def chart(request):
    return render(request, 'Admin/chart.html')