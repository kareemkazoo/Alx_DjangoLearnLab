from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # الأعمدة اللي هتظهر
    list_filter = ('author', 'publication_year')           # فلترة حسب المؤلف والسنة
    search_fields = ('title', 'author')                    # البحث حسب العنوان أو المؤلف

# تسجيل الـ model مع التخصيص
admin.site.register(Book, BookAdmin)
