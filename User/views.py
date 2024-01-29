from django.shortcuts import render

# Create your views here.

def userindex(request):
    return render(request, 'User/userindex.html')

def upload(request):
    return render(request, 'User/upload.html')

def service(request):
    return render(request, 'User/service.html')

def about(request):
    return render(request, 'User/about.html')

def contact(request):
    return render(request, 'User/contact.html')

def team(request):
    return render(request, 'User/team.html')

def testimonial(request):
    return render(request, 'User/testimonial.html')
