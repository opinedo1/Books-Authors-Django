from django.shortcuts import render, HttpResponse, redirect
from .models import Author, Book

# Create your views here.
def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def create_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/')

def create_author(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/authors')

def view_book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'authors': Book.objects.get(id=book_id).authors.all()
    }
    return render(request, 'book.html', context)

def view_author(request, author_id):
    context = {
        'author': Author.objects.get(id=author_id),
        'books': Author.objects.get(id=author_id).books.all()
    }
    return render(request, 'author.html', context)
