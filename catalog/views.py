from django.shortcuts import render

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Modify the view to generate counts for genres and books that contain a particular word (case insensitive)
    num_books_with_banana_in_the_title = Book.objects.filter(title__icontains='banana').count()
    num_genres_with_fiction_in_the_name = Genre.objects.filter(name__icontains='fiction').count()

    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_with_banana_in_the_title': num_books_with_banana_in_the_title,
        'num_genres_with_fiction_in_the_name': num_genres_with_fiction_in_the_name
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book