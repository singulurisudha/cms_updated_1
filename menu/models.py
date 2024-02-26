from django.db import models
from django.utils.text import slugify

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    link = models.URLField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.name)
        super(MenuItem, self).save(*args, **kwargs)
