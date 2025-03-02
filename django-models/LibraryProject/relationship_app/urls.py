from django.urls import path
from relationship_app import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),
]