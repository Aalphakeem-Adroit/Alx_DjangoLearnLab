from django.contrib import admin
from .models import Book

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # show in list view
    list_filter = ("publication_year", "author")  # add filters
    search_fields = ("title", "author")  # enable search
