from bookshelf.models import Book

# Retrieve the book
retrieved_book = Book.objects.get(title="1984") # using get to retrive the book by title.
print(retrieved_book.title)
print(retrieved_book.author)
print(retrieved_book.publication_year)
print(retrieved_book.id) # print the id of the book.

# Or retrieve all books (if you have more):
# all_books = Book.objects.all()
# for book in all_books:
#     print(book.title, book.author, book.publication_year)

# Expected Output (in a comment):
# 1984
# George Orwell
# 1949
# 1