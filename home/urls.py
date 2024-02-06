from . import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.user_login,name='login'),
    path('admin',views.admin_dashboard,name='admin_dashboard'),
    path('Register',views.register,name='register'),
    path('Government',views.Government,name='Government'),
    path('Normal_page',views.Normal_page,name='Normal_page'),
    path('login_user',views.login_user,name='login_user'),
]