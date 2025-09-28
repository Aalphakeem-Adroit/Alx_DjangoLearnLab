from django.db import models

# Create your models here.
class Author(models.Model):
    """
    The Author model represents a book author.
    
    Fields:
        name (CharField): Stores the full name of the author.
    
    Relationships:
        An Author can have multiple related Book objects (one-to-many relationship).
        This is linked using the ForeignKey field defined in the Book model.
    """
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model represents a single book in the system.

    Fields:
        title (CharField): Stores the title of the book.
        publication_year (DateField): Stores the year (and optionally full date) 
            when the book was published. Validated in the serializer to ensure it 
            is not a future date.
        author (ForeignKey): Creates a many-to-one relationship with the Author model. 
            - Each book is linked to a single author.
            - The 'related_name="books"' allows reverse lookup so that we can access 
              all books written by an author using 'author.books'.

    Relationships:
        Author → Book: One author can have many books, 
        but each book must be linked to exactly one author.
    """
    
    title=models.CharField(max_length=200)
    publication_year=models.DateField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')

    def __str__(self):
        return self.title