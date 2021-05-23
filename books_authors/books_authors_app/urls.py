from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('books/<int:book_id>', views.view_book)
]
