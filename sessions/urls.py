from django.urls import include, path
from . import views

urlpatterns = [
    path("sessionhome/", views.sessionhome, name='sessions'),
    
]