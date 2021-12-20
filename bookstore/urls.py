from django.urls import path
from . import views

urlpatterns = [


    path('books/', views.BookListView.as_view(), name='book_view'),
    path('books/<int:id>/', views.BookDetailView.as_view(), name='book_detail_view'),
    path('books/<int:id>/update', views.BookUpdateView.as_view(), name='book_update_view'),
    path('books/<int:id>/delete', views.BookDeleteView.as_view(), name='book_delete_view'),
    path('add-book/', views.BookCreateView.as_view(), name='add_book_view'),


    # path('books/', views.get_books, name='books_view'),
    # path('books/<int:id>/', views.book_detail, name='book_detail_view'),
    # path('add-book/', views.add_book, name='add_book_view'),
    # path('create-comment/<int:id>/', views.create_comment, name='create_comment_view'),

]
