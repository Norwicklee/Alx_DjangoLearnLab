>>> from bookshelf.models import Book
>>> 
>>> # CREATE
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book)
1984
>>> print(book.id)
4
>>>
>>> # RETRIEVE (using the ID from the CREATE step)
>>> retrieved_book = Book.objects.get(id=book.id)
>>> print(retrieved_book.title)
1984
>>> print(retrieved_book.author)
George Orwell
>>> print(retrieved_book.publication_year)
1949
>>> print(retrieved_book.id)
4
>>>
>>> # UPDATE (using the *same* retrieved_book variable)
>>> retrieved_book.title = "Nineteen Eighty-Four"
>>> retrieved_book.save()
>>> print(retrieved_book.title)
Nineteen Eighty-Four
>>>
>>> # DELETE (using the *same* retrieved_book variable)
>>> retrieved_book.delete()
(1, {'bookshelf.Book': 1})
>>> all_books = Book.objects.all()
>>> print(all_books)
<QuerySet [<Book: 1984>, <Book: 1984>, <Book: 1984>]>