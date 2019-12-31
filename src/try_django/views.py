from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    Mtitle = "Aqui..."
    return render(request,"hello_world.html",{"title":Mtitle})

def about_page(request):
    return render(request,"hello_world.html",{"title":"About"})


def contatc_page(request):
    return render(request,"hello_world.html",{"title":"Fale Conosco"})