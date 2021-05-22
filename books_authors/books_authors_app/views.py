from django.shortcuts import render, HttpResponse, redirect
from .models import Author, Book

# Create your views here.
def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)

def view_book(request, book_id):
    context = {
        'books': Book.objects.all(),
        'authors':Author.objects.all()
    }
    return render(request, 'book.html', context)