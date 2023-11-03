from django.shortcuts import render
from django.shortcuts import render,redirect
# from .models import Account
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate,login as django_login , logout as django_logout
from django.contrib.auth import get_user_model
# from django.contrib.auth import authenticate, login, logout



# Create your views here.
# add
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
                # Check if username or email is already taken
        try:
            user = get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            pass
        else:
            messages.error(request, 'this username was tacken ,try another username')
            return render(request, 'accounts/login.html')

        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            pass
        else:
            messages.error(request, 'this email address was tacken ,try another email address')
            return render(request, 'accounts/login.html')

        user = User.objects.create_user(username, email, password)
        messages.add_message(request, messages.INFO, f"your account was created successfully!")
        django_login(request ,user)
        return redirect('index')

    return redirect(reverse("accounts/login.html"))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request,user)
            messages.info(request, "your login successfully!")
            return redirect('index')
        else:
             messages.warning(request, "invalid username or password!")

    return render(request, 'accounts/login.html')

def logout(request):
    django_logout(request)
    messages.add_message(request, messages.INFO, f"you logout from your account.")
    return redirect('index')
# end add

# def login(request):
#     if request.method == "GET":
#         return render(request,"accounts/login.html",{})
#     else:
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = authenticate(request,username=username, password=password,email=email)   
#         if user is not None:
#             django_login(request, user=user)
#             messages.add_message(request, messages.INFO, f"your login successfully!")
#             return redirect(reverse("index"))
        
#         else:
#             messages.add_message(request, messages.ERROR, f"invalid account!!!")
 
#         return redirect(reverse("accounts/login.html"))

# def signup(request):
#     if request.method == "GET":
#         return render(request,"accounts/login.html",{})

#     elif request.method == "POST":
#         user = request.POST["user"]
#         email = request.POST["email"]
#         password = request.POST["password"]        
#         account = Account.objects.create(user=user,email=email,password=password)
#         account.save()
#         messages.add_message(request, messages.INFO, f"your account was created successfully!")

#         return redirect(reverse("index"))