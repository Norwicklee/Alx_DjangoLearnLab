from bookshelf.models import Book

# Nineteen Eighty-Four
#from bookshelf.models import Book
retrieved_book = Book.objects.get(id=book.id) # Or however you retrieve the book instance
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title)

# Expected Output:
# Nineteen Eighty-Four  <-- This is the crucial part!