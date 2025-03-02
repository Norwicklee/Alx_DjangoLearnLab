from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

# Class-based view for Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    return render(request, "logout.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

from django.contrib.auth.decorators import user_passes_test

def admin_view(request):
    if not request.user.userprofile.role == "Admin":
        return HttpResponse("Unauthorized", status=403)
    return HttpResponse("Admin Panel")

def librarian_view(request):
    if not request.user.userprofile.role == "Librarian":
        return HttpResponse("Unauthorized", status=403)
    return HttpResponse("Librarian Dashboard")

def member_view(request):
    if not request.user.userprofile.role == "Member":
        return HttpResponse("Unauthorized", status=403)
    return HttpResponse("Member Dashboard")
