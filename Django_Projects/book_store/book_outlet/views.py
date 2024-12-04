from django.shortcuts import render, get_object_or_404
from datetime import date
from book_outlet.models import Books
from django.db.models import Avg

# Create your views here.
def index(request):
    current_year = date.today().year
    all_books = Books.objects.all().order_by('title')
    num_books = all_books.count()
    avg_rating = all_books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {
        'year': current_year, 
        'books': all_books,
        'total_book_count': num_books,
        'avg_rating': avg_rating
    })
    
def book_details(request, slug):
    book = get_object_or_404(Books, slug=slug)
    return render(request, 'book_outlet/book_details.html',{
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestseller
    })