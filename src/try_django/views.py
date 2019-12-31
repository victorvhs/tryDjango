from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,"hello_world.html")

def about_page(request):
    return HttpResponse("<h1> Sobre</h1>")


def contatc_page(request):
    return HttpResponse("<h1>contato</h1>")