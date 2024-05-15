# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout  # Import authenticate and login
# from django.contrib.auth.models import User


# # Create your views here.
# def home(request):
#     return render(request, 'users/home.html')

# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, username=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid email or password')
#             return redirect('login')
#     return render(request, 'users/login.html')

# def signup(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         phone_number = request.POST['phone_number']
#         email = request.POST['email']
#         password = request.POST['password']
        
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email has already been used')
#             return redirect('signup')
#         else:
#             user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number)
#             messages.success(request, 'Account created successfully. You can now log in.')
#             return redirect('login')
#     return render(request, 'users/signup.html')




# def user_logout(request):
#     logout(request)
#     return redirect('home') 

    
# def forgotpassword(request):
#     return render(request, 'users/forgotpassword.html')

# def testing(request):
#     return render(request, 'users/index.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

User = get_user_model()


def home(request):
    return render(request, 'users/home.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if not user.is_doctor:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Access restricted to patients.")
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')




def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Simple validation checks
        if not first_name or not last_name or not email or not password:
            messages.error(request, "Please fill out all required fields.")
            return redirect('signup')

        # Check if the user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already used.")
            return redirect('login')

        # Create the user
        user = User.objects.create(
            username=email,  # Assuming username is the email
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password),
            is_user=True,  # Set this as True for all user signups
            is_doctor=False,  # Ensure this is False for regular users
            phone_number=phone_number
        )
        user.save()

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'users/signup.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def forgotpassword(request):
    return render(request, 'users/forgotpassword.html')


def testing(request):
    return render(request, 'users/index.html')



def user_visits(request):
    return render(request, 'users/visits.html')


def aboutus(request):
    return render(request, 'pages/aboutus.html')

def doctor_messages(request):
    # Your view logic here
    return render(request, 'doctors/messaging/doctormessage.html')
