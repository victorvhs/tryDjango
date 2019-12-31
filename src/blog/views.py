from django.http import( Http404 ,HttpResponseBadRequest)
from django.shortcuts import render , get_object_or_404
from .models import  BlogPost

def blog_post_detail_page(request, slug):
    #"""queryset = BlogPost.objects.filter(slug=slug)
    #if queryset.count() == 0:
    #    raise Http404
    #obj = queryset.first()
    #"""
    obj = get_object_or_404(BlogPost,slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"post" : obj}
    return render(request,template_name,context)

def blog_post_list_view(request):
    # list out objects 
    # could be search
    qs = BlogPost.objects.all()
    template_name = 'blog_post_list.html'
    context = {'object_list': qs}
    return render(request, template_name, context) 



def blog_post_create_view(request):
    # create objects
    # ? use a form
    template_name = 'blog_post_create.html'
    context = {'form': None}
    return render(request, template_name, context)  


def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)   


def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)  


def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete.html'
    context = {"object": obj}
    return render(request, template_name, context)  

