from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import EventRegistration
#from rest_framework import generics


import EventApp

def EventRegistration_list(request):
    polls=EventRegistration.objects.all()
    data={"results":list(polls.values('firstname','lastname','email','mobile','address'))}
    return JsonResponse(data)

