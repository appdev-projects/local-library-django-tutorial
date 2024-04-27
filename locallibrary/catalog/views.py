from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Author, BookInstance, Genre
from .forms import BookForm

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

class BookListView(LoginRequiredMixin, generic.ListView):
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

class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("book-detail", pk=book.pk)
    else:
        form = BookForm()
    
    context = {"form": form}

    return render(request, "catalog/book_form.html", context=context)

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book-detail", pk=book.pk)
    else:
        form = BookForm(instance=book)

    context = {"form": form}

    return render(request, "catalog/book_form.html", context=context)

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("books")

class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    context_object_name = "authors"
    paginate_by = 5

class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )
