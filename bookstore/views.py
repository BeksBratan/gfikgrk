from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


class BookListView(generic.ListView):
    template_name = 'bookstore/book_list.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()




class BookDetailView(generic.DetailView):
    template_name = 'bookstore/book_detail.html'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)




class BookCreateView(generic.CreateView):
    template_name = 'bookstore/add_book.html'
    form_class = forms.BookForm
    success_url = '/books/'
    queryset = models.Book.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)




class BookUpdateView(generic.UpdateView):
    template_name = 'bookstore/add_book.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)




class BookDeleteView(generic.DeleteView):
    template_name = 'bookstore/book_delete.html'
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)























# from django.http import Http404, HttpResponse
# from django.shortcuts import render, redirect
# from . import models, forms


# def get_books(request):
#     book = models.Book.objects.all()
#     return render(request, 'bookstore/book_list.html', {'book': book})


# def book_detail(request, id):
#     try:
#         book = models.Book.objects.get(id=id)
#         try:
#             comment = models.Comment.objects.filter(book_id=id).order_by('created_date')
#         except models.Comment.DoesNotExist:
#             return HttpResponse('No comments!')
#     except models.Book.DoesNotExist:
#         raise Http404('Post does not exist, buddy!')
#     return render(request, 'bookstore/book_detail.html', {'book': book, 'book_comment': comment, 'redirect_path': id})


# def add_book(request):
#     if request.method == "POST":
#         form = forms.BookForm(request.POST, request.FILES)
#         print(form.data)
#         if form.is_valid():
#             form.save()
#             print('Book added successfully!')
#             return redirect('books_view')
#     else:
#         form = forms.BookForm()
#     return render(request, 'bookstore/add_book.html', {'form': form})


# def create_comment(request, id):
#     if request.method == 'POST':
#         form = forms.CommentForm(request.POST, request.FILES)
#         print(form.data)
#         if form.is_valid():
#             form.save()
#             return redirect(f'/books/{id}')
#     else:
#         form = forms.CommentForm()
#     return render(request, 'bookstore/create_comment.html', {'form': form})
