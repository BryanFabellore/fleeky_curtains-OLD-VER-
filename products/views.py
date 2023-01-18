from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def view_products (request):
    template = loader.get_template("products.html")
    return HttpResponse(template.render())

def checkout (request):
    template = loader.get_template("checkout.html")
    return HttpResponse(template.render())
