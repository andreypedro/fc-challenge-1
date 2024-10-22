from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'core/blog_list.html', {'posts': posts})