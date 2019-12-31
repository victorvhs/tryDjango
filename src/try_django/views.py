from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1> Ta aqui</h1>")

def about_page(request):
    return HttpResponse("<h1> Sobre</h1>")


def contatc_page(request):
    return HttpResponse("<h1>contato</h1>")