### 📄 `retrieve.md`
```markdown
# Retrieve Operation

## Command
```python
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author)


Expected Output:
1984 George Orwell
