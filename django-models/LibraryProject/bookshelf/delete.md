#from bookshelf.models import Book

retrieved_book.delete()  # retrieve the book instance and delete it
all_books = Book.objects.all()
print(all_books)

# Expected Output:
# <QuerySet []>  <-- This is the crucial part!