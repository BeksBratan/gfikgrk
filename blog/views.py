from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Posts, Comments


def hello(request):
    return HttpResponse('Hello Python!')


def get_posts(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'post_list.html', context)


def comments(request):
    context = {
        'comments': Comments.objects.all()
    }
    return render(request, 'comments.html', context)
