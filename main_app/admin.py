from django.contrib import admin
# import your models here
from .models import Group, User, Expense

# Register your models here
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Expense)
