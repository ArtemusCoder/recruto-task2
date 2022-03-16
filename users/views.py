from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from random import randint
from django.contrib.auth import logout



def number(request):
    if request.user.is_authenticated:
        x = randint(1000, 9999)
        logout(request)
        return HttpResponse(str(x))
    else:
        return HttpResponse("You need to login")
