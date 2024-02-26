# models.py
from django.db import models
from django.contrib.auth.models import User
from cms_project import settings

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
        
    ]
    id=models.AutoField(primary_key=True)
    issue = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name = "created_by_ticket",null=True)
    solution=models.TextField()
    updated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name = "updated_by_ticket",null=True)
    

    def __str__(self):
        return self.issue
