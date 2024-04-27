from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Book, Author, BookInstance, Genre

@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()

    # case insensitive regex filter
    num_books_with_teacher = Book.objects.filter(title__iregex=r'teacher').count()

    # A dictionary we can pass to the template
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_with_teacher': num_books_with_teacher
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    """Class Based View for books"""
    model = Book
    context_object_name = "books"
    paginate_by = 10

    # def get_queryset(self):
    #     return Book.objects.filter(author=Author.objects.get(last_name="Kim"))

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context["num_books"] = Book.objects.count()
        return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = "authors"
    paginate_by = 5

class AuthorDetailView(generic.DetailView):
    model = Author
