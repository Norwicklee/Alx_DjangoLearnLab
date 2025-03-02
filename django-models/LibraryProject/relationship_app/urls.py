
from django.urls import path
from django.shortcuts import redirect
from relationship_app import views
from .views import list_books
from .views import LibraryDetailView
from .views import user_login, user_logout, user_register, home

def redirect_to_books(request):
    return redirect('list_books') #or redirect('/relationship/books/')
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path("login/", user_login, name="login"),
    path('', redirect_to_books, name='relationship_home'),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
]


