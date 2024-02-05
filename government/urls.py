from . import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.gov,name='gov'),
    path('document', views.document, name='document')


]