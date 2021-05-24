from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('books/<int:book_id>', views.view_book),
    path('create_book', views.create_book),
    path('authors', views.authors),
    path('authors/<int:author_id>', views.view_author),
    path('create_author', views.create_author),
    # Assigns books or authors to to the element being viewed
    path('books/<int:book_id>/addauthor', views.addauthor),
    path('authors/<int:author_id>/addbook', views.addbook),
    
]
