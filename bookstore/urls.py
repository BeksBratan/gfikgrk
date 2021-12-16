from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books, name='books_view'),
    path('books/<int:id>/', views.book_detail, name='book_detail_view'),
    path('add-book/', views.add_book, name='add_book_view'),
    path('create-comment/<int:id>/', views.create_comment, name='create_comment_view'),

]
