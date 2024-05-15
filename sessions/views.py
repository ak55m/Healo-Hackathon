from django.shortcuts import render, redirect
# from django.contrib import messages


def sessionhome(request):
    return render(request, 'sessions/sessionhome.html')




