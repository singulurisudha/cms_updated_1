from django.db import models
from django.contrib.auth.models import AbstractUser


from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    id=models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    mobile_number=models.IntegerField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
        
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email



class Role(models.Model):
    id=models.AutoField(primary_key=True)
    role = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='roles', blank=True)
    
    def __str__(self):
        return self.role
    
class Permission(models.Model):
    modules = models.ManyToManyField('Module', related_name='permissions')
    roles = models.ManyToManyField('Role',max_length=255)

    def __str__(self):
        role_name= ', '.join(str(role) for role in self.roles.all())
        return f"permission for role: {role_name}"
    
class Module(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.name