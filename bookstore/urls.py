from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books, name='book_view'),
    path('books/<int:id>/', views.book_detail, name='book_detail_view'),
    path('books/create/', views.create_book, name='book_create')

]