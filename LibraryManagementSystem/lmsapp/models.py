from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
 
    def __str__(self):
        return f"{self.name}"
    
class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    genre=models.CharField(max_length=100)
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    available_copies = models.IntegerField()

    def __str__(self):
        return self.title

class Membership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.plan_name} Plan"