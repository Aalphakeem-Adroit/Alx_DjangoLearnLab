# Delete Operation

## Command
```python
from bookshelf.models import Book
retrieved_book.delete()
```

## Expected Output:
```
(1, {'bookshelf.Book': 1})
# The book instance has been deleted.
```

## Verification:
```python
Book.objects.all()
```

## Expected Output:
```shell
<QuerySet []>
# Empty queryset confirms deletion.
```
