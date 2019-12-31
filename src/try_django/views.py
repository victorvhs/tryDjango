from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    Mtitle = "Aqui..."
    context ={"title":Mtitle, "produtos":["solidão","tristeza","dor"]}
    return render(request,"home.html",context)

def about_page(request):
    return render(request,"about.html",{"title":"About"})


def contatc_page(request):
    return render(request,"hello_world.html",{"title":"Fale Conosco"})