# Update Book

```python
from bookshelf.models import Book

# جلب الكتاب اللي عنوانه "1984"
book = Book.objects.get(title="1984")

# تعديل العنوان وحفظ التغيير
book.title = "Nineteen Eighty-Four"
book.save()

# عرض الكتاب بعد التعديل
book
```

**Expected Output:**
```
<Book: Nineteen Eighty-Four>
```
