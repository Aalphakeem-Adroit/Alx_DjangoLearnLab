# CRUD Operations in Django Shell

This document contains the full set of CRUD (Create, Retrieve, Update, Delete) operations performed on the `Book` model in the Django shell.

---

## Create
```python
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

## Retrieve
>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.title, book.author, book.publication_year
('1984', 'George Orwell', 1949)

## Update
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title
'Nineteen Eighty-Four'

## Delete

>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
