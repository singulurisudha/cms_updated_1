from django.db import models
from cms_project import settings

class Category(models.Model):
    id=models.AutoField(primary_key=True)
<<<<<<< HEAD
    category = models.CharField(max_length=100,unique=True)
=======
    category = models.CharField(max_length=100)
>>>>>>> 1103a6d72f00a37c7610cfaf2dd1621e0293f610
    
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
<<<<<<< HEAD
    archive=models.BooleanField(default=False)
=======
>>>>>>> 1103a6d72f00a37c7610cfaf2dd1621e0293f610

    def __str__(self):
        return self.title
