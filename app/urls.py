from django.urls import path
from .views import create_book, list_books, detail_book, update_book, delete_book

urlpatterns = [
    path('', create_book, name='create_book'),
    path('list_books/', list_books, name='list_books'),
    path('list_books/<id>', detail_book, name='detail_book'),
    path('list_books/<id>/update', update_book, name='update_book'),
    path('list_books/<id>/delete', delete_book, name='delete_book'),
]
