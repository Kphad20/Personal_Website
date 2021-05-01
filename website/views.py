from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'home.html', {'blogs':blogs})

def blog(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog.html', {'blogs':blogs})

def blog_detail(request, blog_id, slug):
    blog = get_object_or_404(Blog, pk=blog_id, slug=slug)
    return render(request, 'blog_detail.html', {'blog':blog})

