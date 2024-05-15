from django.shortcuts import render, redirect
# from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

User = get_user_model()


def doctormessage(request):
    # Logic to retrieve doctor messages
    return render(request, 'messaging/doctormessage.html')

def usermessage(request):
    # Logic to retrieve user messages
    return render(request, 'messaging/usermessage.html')

