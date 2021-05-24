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
        'authors': Book.objects.get(id=book_id).authors.all(),
        # exclude authors who are already assigne to the book
        'all_authors': Author.objects.exclude(books__id=book_id)
    }
    return render(request, 'book.html', context)

def view_author(request, author_id):
    context = {
        'author': Author.objects.get(id=author_id),
        'books': Author.objects.get(id=author_id).books.all(),
        'all_books': Book.objects.exclude(authors__id=author_id)
    }
    return render(request, 'author.html', context)

# assigns an author to a book
def addauthor(request, book_id):
    this_author = request.POST['author_id']
    this_book = Book.objects.get(id=book_id)
    this_book.authors.add(this_author)
    return redirect('/authors/{}'.format(request.POST['author_id']))

# assigns a book to an author
def addbook(request, author_id):
    print(request.POST)
    this_book = request.POST['book_id']
    this_author = Author.objects.get(id=author_id)
    this_author.books.add(this_book)
    return redirect('/books/{}'.format(request.POST['book_id']))