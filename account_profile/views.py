from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def view_profile (request):
    template = loader.get_template("account_profile.html")
    return HttpResponse(template.render())

