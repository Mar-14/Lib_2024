from django.contrib import admin

from .models import Author, Book, Membership, Payment, category

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(category)
admin.site.register(Membership)
admin.site.register(Payment)