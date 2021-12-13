from django.http import Http404
from django.shortcuts import render, redirect
from . import models, forms


def get_books(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})


def book_detail(request, id):
    try:
        book = models.Book.objects.get(id=id)
    except models.Book.DoesNotExist:
        raise Http404('Post does not exist!')
    return render(request, 'book_detail.html', {'book': book})


def create_book(request):
    if request.method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_view')
    else:
        form = forms.BookForm()
    return render(request, 'book_create.html', {'form': form})
