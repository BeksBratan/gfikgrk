from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from . import models, forms


# def get_posts(request):
#     context = {
#         'posts': Posts.objects.all()
#     }
#     return render(request, 'post_list.html', context)

def get_posts(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})


def post_detail(request, id):
    try:
        post = models.Post.objects.get(id=id)
        try:
            comment = models.Comments.objects.filter(post_id=id).order_by('created_date')
        except models.Comments.DoesNotExist:
            return HttpResponse('No Comments')

    except models.Post.DoesNotExist:
        raise Http404('Post does not exist, baby')

    return render(request, 'post_detail.html', {'post': post, 'post_comment': comment})


def comments(request):
    context = {
        'comments': models.Comments.objects.all()
    }
    return render(request, 'comments.html', context)


def add_post(request):
    method = request.method
    if method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        print(form.data)
        models.Post.objects.create(title=form.data['title'],
                                   description=form.data['description'],
                                   image=form.data['image'])
        return HttpResponse('Post Created Successfully')
        # return redirect('post_view')
    else:
        form = forms.PostForm()

    return render(request, 'add_post.html', {'form': form})


def add_comment(request):
    method = request.method
    if method == 'POST':
        form = forms.CommentForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponse('Comment created successfully')
    else:
        form = forms.CommentForm
    return render(request, 'add_comment.html', {'form': form})
