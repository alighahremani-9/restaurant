from django.shortcuts import render,redirect
from .models import Book
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request , "blog/index.html",{})

def about(request):
    return render(request,"blog/about.html",{})

def booking(request):
    return render(request,"blog/booking.html",{})

def contact_us(request):
    return render(request,"blog/contact.html",{})

def menu(request):
    return render(request,"blog/menu.html",{})

def service(request):
    return render(request,"blog/service.html",{})

def team(request):
    return render(request,"blog/team.html",{})

def testimonial(request):
    return render(request,"blog/testimonial.html",{})

# def booktable(request):
#     return render(request,"blog/booktable.html",{})
@login_required
def booktable(request):
    if request.method == "GET":
        return render(request,"blog/booktable.html",{})

    elif request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        number = request.POST["number"]        
        book = Book.objects.create(name=name,email=email,number=number)
        book.save()
        messages.add_message(request, messages.INFO, f"your request of booking was saved!")
        return redirect(reverse("booktable"))