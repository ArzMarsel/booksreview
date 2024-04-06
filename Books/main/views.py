from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import ReviewForm
from .models import Author, Book, Review


def index(request):
    book = Book.objects.all()
    return render(request, 'h1.html', {'book': book})


def index_author(request):
    book = Book.objects.order_by('author')
    return render(request, 'h1.html', {'book': book})


def index_date(request):
    book = Book.objects.order_by('date_of_pub')
    return render(request, 'h1.html', {'book': book})


def index_name(request):
    book = Book.objects.order_by('title')
    return render(request, 'h1.html', {'book': book})


def author1(request):
    aut = Author.objects.all()
    return render(request, 'authors.html', {'author': aut})


class More1(DetailView):
    model = Book
    template_name = 'more_book.html'
    context_object_name = 'book'


class More2(DetailView):
    model = Author
    template_name = 'more_author.html'
    context_object_name = 'author'


def review(request):
    model = Review.objects.all()
    return render(request, 'review.html', {"review": model})


def rate(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
            form = ReviewForm()
    return render(request, 'rate.html', {'form': form})