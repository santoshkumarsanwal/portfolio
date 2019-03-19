from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import blog


def allblogs(request):
    blogs = blog.objects
    return render(request, 'blog/allblog.html', {'blogs': blogs})

def detail(request, blog_id):
     detailblog=get_object_or_404(blog, pk=blog_id)
     return render(request, 'blog/detail.html', {'blog':detailblog})