# Retrieve Book

```python
from bookshelf.models import Book

# جلب الكتاب باستخدام get
book = Book.objects.get(title="1984")  # لازم يكون نفس العنوان اللي استخدمته عند الإنشاء
book

