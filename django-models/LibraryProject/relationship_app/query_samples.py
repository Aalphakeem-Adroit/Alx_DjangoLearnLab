import sys
import django
import os

# Add parent folder to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return list(author.books.all())
    except Author.DoesNotExist:
        return []

# 2. List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return list(library.books.all())
    except Library.DoesNotExist:
        return []

# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None

# Example usage
if __name__ == "__main__":
    print("Books by Author1:", books_by_author("Author1"))
    print("Books in Library1:", books_in_library("Library1"))
    print("Librarian of Library1:", librarian_of_library("Library1"))
