from django.shortcuts import render
from . import models


# def get_posts(request):
#     context = {
#         'posts': Posts.objects.all()
#     }
#     return render(request, 'post_list.html', context)

def get_posts(request):
    post = models.Posts.objects.all()
    return render(request, 'post_list.html', {'post': post})


def comments(request):
    context = {
        'comments': models.Comments.objects.all()
    }
    return render(request, 'comments.html', context)
