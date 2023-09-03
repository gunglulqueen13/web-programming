from django.shortcuts import render
from django import template
from django.conf import settings


def home(request):
    data = {"STATIC_URL": settings.STATIC_URL}
    return render(request, "templates/static_handler.html", context=data)
