from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

User = get_user_model()


def home(request):
    return render(request, 'doctors/home.html')


def doctor_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            if user.is_doctor:
                login(request, user)
                request.session['is_doctor'] = True  # Set a flag specifically for doctors
                return redirect('doctorhome')  # Redirect to doctor's dashboard
            else:
                # If the user is not a doctor, do not allow them to log in here
                if user.is_admin:
                    error_message = "Admin accounts cannot access doctor areas."
                else:
                    error_message = "Unauthorized access. Only doctors can log in here."
                messages.error(request, error_message)
                return redirect('doctorlogin')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('doctorlogin')
    return render(request, 'doctors/login.html')



def doctor_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Simple validation checks
        if not first_name or not last_name or not email or not password:
            messages.error(request, "Please fill out all required fields.")
            return redirect('doctorsignup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already used.")
            return redirect('doctorsignup')

        user = User.objects.create(
            username=email,  # Assuming username is the email
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password),
            is_doctor=True,
            is_user=False,  # Make sure this is set to False for doctors
            phone_number=phone_number
        )
        user.save()

        messages.success(request, "Physician account created successfully. Please log in.")
        return redirect('doctorlogin')

    return render(request, 'doctors/signup.html')


def doctor_logout(request):
    logout(request)
    return redirect('doctorhome')

def doctor_forgotpassword(request):
    return render(request, 'doctors/forgotpassword.html')

def testing(request):
    return render(request, 'doctors/index.html')

def doctor_visits(request):
    return render(request, 'doctors/visits.html')

def doctor_aboutus(request):
    return render(request, 'pages/daboutus.html')




# def doctor_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, username=email, password=password)
        
#         if user is not None:
#             if user.is_doctor:  # Assuming you have a field 'is_doctor' in your custom user model
#                 login(request, user)
#                 return redirect('doctorhome')
#             else:
#                 messages.error(request, 'You are not authorized to access this page.')
#                 return redirect('login')
#         else:
#             messages.error(request, 'Invalid email or password')
#             return redirect('doctorlogin')
#     return render(request, 'doctors/login.html')

# def doctor_signup(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         phone_number = request.POST.get('phone_number')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email has already been used')
#             return redirect('doctorsignup')
#         else:
#             # Create the doctor user
#             user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number, is_doctor=True)
#             if user:
#                 messages.success(request, 'Account created successfully. You can now log in.')
#                 return redirect('doctorlogin')
#             else:
#                 messages.error(request, 'An error occurred while creating your account.')
#     return render(request, 'doctors/signup.html')