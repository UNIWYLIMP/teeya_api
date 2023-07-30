from django.http import JsonResponse
from .models import *
from django.shortcuts import redirect


def index(request):
    return redirect("https:www.teeya.tech")


def create_contact(request):
    if request.method == 'GET':
        Name = request.GET.get('Name')
        Email = request.GET.get('Email')
        Tel = request.GET.get('Tel')
        Description = request.GET.get('Description')
        new_contact = Contact(Name=Name, Email=Email, Telephone=Tel, QueryDescription=Description)
        new_contact.save()
        return JsonResponse({"message": "Request Processed"})

    else:
        return JsonResponse({"message": "Request Invalid"})


def create_booking(request):
    if request.method == 'GET':
        Name = request.GET.get('Name')
        Email = request.GET.get('Email')
        Tel = request.GET.get('Tel')
        ProjectDescription = request.GET.get('Description')
        ProductName = request.GET.get('ProductName')
        new_booking = Booking(Name=Name, Email=Email, Telephone=Tel, ProjectDescription=ProjectDescription,
                              ProductName=ProductName)
        new_booking.save()
        return JsonResponse({"message": "Request Processed"})

    else:
        return JsonResponse({"message": "Request Invalid"})
