from bookshelf.models import Book

# Update the title
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()  # Important: Save the changes!
print(book_to_update.title)

# Expected Output (in a comment):
# Nineteen Eighty-Four