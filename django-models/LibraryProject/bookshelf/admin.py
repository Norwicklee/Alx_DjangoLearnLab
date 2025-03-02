from django.contrib import admin

# Register your models here.
from .models import Book  # Import your Book model

admin.site.register(Book) #This registers the Book model with the Django admin, making it manageable through the admin interface.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in list view
    list_filter = ('publication_year',)  # Add filters based on publication year
    search_fields = ('title', 'author')  # Add search fields for title and author