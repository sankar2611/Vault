from . import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('chart/', views.chart, name='chart')


]