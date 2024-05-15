from django.urls import include, path
from . import views

urlpatterns = [
    #for the users
    path("", views.home, name='doctorhome'),
    # path("", views.home, name='home'),
    path("logout/", views.doctor_logout, name='doctorlogout'),
    path("login/", views.doctor_login, name='doctorlogin'),
    path("signup/", views.doctor_signup, name='doctorsignup'),
    path("forgotpassword/", views.doctor_forgotpassword, name='doctorforgotpassword'),
    path("testing/", views.testing, name='testingpages'),
    path("visits/", views.doctor_visits, name='doctorvisits'),
    path("aboutus/", views.doctor_aboutus, name='doctoraboutus'),
    # path('messages/', views.doctor_messages, name='doctor_messages'),



]