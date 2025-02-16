from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)  # Output: 1984 (or the string representation you defined in __str__)
print(book.id) #Output the id of the book instance

# Expected Output (in a comment):
# 1984
# 1