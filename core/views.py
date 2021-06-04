from django.shortcuts import render
from .models import Posts
# Create your views here.


def index(request):
    postagens = Posts.objects.all()

    context = {
        'posts': postagens,
    }

    return render(request, 'index.html', context)


def blog(request):
    return render(request, 'blog.html')


def contato(request):
    return render(request, 'contato.html')


def posts(request):
    return render(request, 'post.html')
