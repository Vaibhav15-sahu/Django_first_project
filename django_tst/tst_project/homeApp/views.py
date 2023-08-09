from django.http import HttpResponse
from django.shortcuts import render

def home_view(req):
    return render(req, 'homeApp/home.html')

def about_view(req):
    return render(req, 'homeApp/about.html')

def contact_view(req):
    return render(req, 'homeApp/contact.html')

def day_view(req, day):
    data = { "Day" : day }
    return render(req, 'homeApp/displayDay.html', data )