from django.urls import include, path
from . import views

urlpatterns = [
    #for the users
    path("", views.home, name='home'),
    path("login/", views.user_login, name='login'),
    path("signup/", views.signup, name='signup'),
    path("logout/", views.user_logout, name='logout'),
    path("visits/", views.user_visits, name='visits'),
    # path("doctor/signup/", views.signup, name='doctorsignup'),
    # path("doctor/home/", views.signup, name='doctorhome'),
    path("forgotpassword/", views.forgotpassword, name='forgotpassword'),
    path("testing/", views.testing, name='testingpages'),
    path("aboutus/", views.aboutus, name='aboutus'),



]