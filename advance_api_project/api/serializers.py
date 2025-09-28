from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    
    Purpose:
        Converts Book model instances into JSON format (serialization)
        and validates/creates/updates Book objects from JSON data (deserialization).

    Fields:
        Includes all fields from the Book model: title, publication_year, and author.

    Validation:
        - Custom validation ensures 'publication_year' is not a future date.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom field-level validation:
        Ensures that the publication year is not in the future.
        """
         
        if value > date.today():
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    Purpose:
        Converts Author model instances into JSON format and handles
        nested serialization of related Book objects.

    Fields:
        - name: The author's name.
        - books: A nested list of BookSerializer objects representing
                 all books related to this author.

    Relationship Handling:
        The 'books' field uses the related_name='books' defined in the Book model's
        ForeignKey field. This allows the serializer to automatically fetch all
        books for a given author and serialize them using BookSerializer.
    """
    
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
