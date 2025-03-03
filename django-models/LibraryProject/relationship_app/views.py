from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpRequest #Ensure that HttpRequest is here.
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def home(request):
    return render(request, 'relationship_app/home.html')

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Change "home" to your desired redirect page
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")  # Change "home" to your desired redirect page
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Admin View")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Librarian View")

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Member View")