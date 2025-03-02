
from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views
from .views import list_books
from .views import LibraryDetailView
from .views import user_login, user_logout, user_register, home

def redirect_to_books(request):
    return redirect('list_books') #or redirect('/relationship/books/')
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', redirect_to_books, name='relationship_home'),
     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
   
]


