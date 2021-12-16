from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from . import models, forms


def get_books(request):
    book = models.Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'book': book})


def book_detail(request, id):
    try:
        book = models.Book.objects.get(id=id)
        try:
            comment = models.Comment.objects.filter(book_id=id).order_by('created_date')
        except models.Comment.DoesNotExist:
            return HttpResponse('No comments!')
    except models.Book.DoesNotExist:
        raise Http404('Post does not exist, buddy!')
    return render(request, 'bookstore/book_detail.html', {'book': book, 'book_comment': comment, 'redirect_path': id})


def add_book(request):
    if request.method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            print('Book added successfully!')
            return redirect('books_view')
    else:
        form = forms.BookForm()
    return render(request, 'bookstore/add_book.html', {'form': form})


def create_comment(request, id):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            return redirect(f'/books/{id}')
    else:
        form = forms.CommentForm()
    return render(request, 'bookstore/create_comment.html', {'form': form})
