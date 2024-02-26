from django.db import models
from cms_project import settings

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    category = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.category

class Content(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name = "created_by_content",null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name = "updated_by_content",null=True)
    image=models.ImageField()
    archive=models.BooleanField(default=False)

    def __str__(self):
        return self.title
