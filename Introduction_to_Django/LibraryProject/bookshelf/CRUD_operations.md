### 📄 `CRUD_operations.md`

````markdown
# CRUD Operations in Django Shell

This document records the step-by-step CRUD (Create, Retrieve, Update, Delete) operations performed on the **Book** model inside the Django shell.

---

## 🟢 Create
### Command
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_date="1949")
````

### Output

```python
# Successfully created Book instance with ID (auto-generated).
# Example: <Book: 1984 by George Orwell>
```

---

## 🔵 Retrieve

### Command

```python
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author)
```

### Output

```python
1984 George Orwell
```

---

## 🟠 Update

### Command

```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title, retrieved_book.author)
```

### Output

```python
Nineteen Eighty-Four George Orwell
```

---

## 🔴 Delete

### Command

```python
retrieved_book.delete()
```

### Output

```python
(1, {'bookshelf.Book': 1})
# The book instance has been deleted.
```

### Verification

```python
Book.objects.all()
```

### Output

```python
<QuerySet []>
# Empty queryset confirms deletion.
```

```