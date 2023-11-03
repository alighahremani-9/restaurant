from django.shortcuts import render,redirect
from .models import Ticket
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def contact(request):
    if request.method == "GET":
        return render(request,"contactus/contact.html",{})

    elif request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        body = request.POST["body"]        
        ticket = Ticket.objects.create(name=name,email=email,body=body)
        ticket.save()
        messages.add_message(request, messages.INFO, f"your massage was saved successfully!")
        return redirect(reverse("contact"))