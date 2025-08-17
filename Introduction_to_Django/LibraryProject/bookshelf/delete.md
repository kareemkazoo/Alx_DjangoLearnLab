# Delete Book

```python
from bookshelf.models import Book

# جلب الكتاب اللي عنوانه "Nineteen Eighty-Four"
book = Book.objects.get(title="Nineteen Eighty-Four")

# حذف الكتاب
book.delete()

# التأكد من عدم وجود كتب
Book.objects.all()
```

**Expected Output:**
```
<QuerySet []>
```
