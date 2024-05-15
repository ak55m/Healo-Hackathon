from django.urls import include, path
from . import views

urlpatterns = [
    path("doctormessage/", views.doctormessage, name='doctor_message'),
    
    path("usermessage/", views.usermessage, name='user_message'),
]