from django.shortcuts import render, HttpResponse, redirect
from .models import Author, Book

# Create your views here.
def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def authors(request):
    return render(request, 'authors.html', {"authors": Author.objects.all()})

def create_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/')

def view_book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'authors': Book.objects.get(id=book_id).authors.all()
    }
    return render(request, 'book.html', context)