from django.shortcuts import render, redirect
from .models import Book, Library, Librarian
from relationship_app.models import Book
from django.views.generic import DetailView
from relationship_app.models import Library
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/books_list.html', {'books': books})

def libraries_list(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/libraries_list.html', {'libraries': libraries})

def librarians_list(request):
    librarians = Librarian.objects.all()
    return render(request, 'relationship_app/librarians_list.html', {'librarians': librarians})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_books')  # Redirect to a desired page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'logout.html')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user automatically after registration
            return redirect('list_books')  # Redirect to a desired page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})