from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from .views import list_books, LibraryDetailView, user_register

def redirect_to_books(request):
    return redirect('list_books')  # or redirect('/relationship/books/')

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', redirect_to_books, name='home'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Fixed this line
    path('register/', user_register, name='register'),
]



