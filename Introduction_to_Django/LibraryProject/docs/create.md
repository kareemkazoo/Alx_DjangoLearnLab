# Create Book

```python
from bookshelf.models import Book

# إنشاء كتاب جديد
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# عرض الكتاب اللي اتعمل
book
```

**Expected Output:**
```
<Book: 1984>
```
