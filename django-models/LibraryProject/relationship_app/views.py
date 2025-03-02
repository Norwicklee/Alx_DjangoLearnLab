from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views.generic import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_detail(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, "relationship_app/library_detail.html", {"library": library})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'




