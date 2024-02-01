from django.db import models

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category

class Content(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='contents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image=models.ImageField()

    def __str__(self):
        return self.title