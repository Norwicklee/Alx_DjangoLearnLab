from bookshelf.models import Book

# Delete the book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

# Try to retrieve all books (should be empty now)
all_books = Book.objects.all()
print(all_books) #Output: <QuerySet []>

# Expected Output (in a comment):
# <QuerySet []>