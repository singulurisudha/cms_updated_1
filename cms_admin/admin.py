# cms_admin/admin.py

from django.contrib import admin
from category.models import Category , Content
from menu.models import MenuItem
from user.models import User
from support.models import Ticket

# Register models
admin.site.register(Category)
admin.site.register(Content)
admin.site.register(MenuItem)
admin.site.register(User)
admin.site.register(Ticket)
