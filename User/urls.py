from . import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.userindex,name='userindex'),
    path('upload/', views.upload, name='upload'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('about/', views.about, name='about'),
    
    

]