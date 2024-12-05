from django.contrib import admin

from .models import Author,category,Book,Membership

# Register your models here.
admin.site.register(Author) 
admin.site.register(category) 
admin.site.register(Book) 
admin.site.register(Membership) 