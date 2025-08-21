from django.contrib import admin
from .models import Book  # مهم: استيراد الموديل هنا

# تخصيص عرض الموديل في الـ Admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # الأعمدة اللي تظهر في القائمة
    search_fields = ('title', 'author')                    # البحث في الأعمدة دي
    list_filter = ('published_date',)                      # فلتر حسب التاريخ

# تسجيل الموديل مع الـ Admin
admin.site.register(Book, BookAdmin)



