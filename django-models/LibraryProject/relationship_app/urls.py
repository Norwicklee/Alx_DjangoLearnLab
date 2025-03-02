from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from .views import list_books, LibraryDetailView, user_register
from django.contrib.auth import views as auth_views
from . import views

def redirect_to_books(request):
    return redirect('list_books')  # or redirect('/relationship/books/')

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', redirect_to_books, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'), #This line is critical.
]



