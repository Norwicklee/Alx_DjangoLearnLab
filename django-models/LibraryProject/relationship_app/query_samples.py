from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    authors = Author.objects.filter(name=author_name)
    if authors:
        for author in authors:
            books = Book.objects.filter(author=author)
            print(f"Books by {author.name}:")
            for book in books:
                print(f"- {book.title}")
    else:
        print(f"Author '{author_name}' not found.")

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in {library_name}:")
        for book in library.books.all():
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for '{library_name}'.")

#Example data creation.
# a1 = Author(name="Author One"); a1.save()
# a2 = Author(name="Author Two"); a2.save()
# b1 = Book(title="Book One", author=a1); b1.save()
# b2 = Book(title="Book Two", author=a1); b2.save()
# b3 = Book(title="Book Three", author=a2); b3.save()
# l1 = Library(name="Library One"); l1.save()
# l1.books.add(b1,b2)
# l2 = Library(name="Library Two"); l2.save()
# l2.books.add(b3)
# librarian1 = Librarian(name="Librarian One", library=l1); librarian1.save()
# librarian2 = Librarian(name="Librarian Two", library=l2); librarian2.save()

#Example query execution.
#query_books_by_author("Author One")
#list_books_in_library("Library One")
#retrieve_librarian_for_library("Library One")