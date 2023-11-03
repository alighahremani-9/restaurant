"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog.views import *
from contactus import urls as contact_url
from accounts import urls as accounts_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name= "index"),
    path('about/', about , name= "about"),
    path('booking/', booking , name= "booking"),
    # path('contactus/',contact_us,name="contact"),
    path('menu/',menu,name="menu"),
    path('service/',service,name="service"),
    path('team/',team,name="team"),
    path('testimonial/',testimonial,name="testimonial"),
    path('book/',booktable,name="booktable"),
    path("contact/",include(contact_url)),
    path("accounts/",include(accounts_url)),
]
