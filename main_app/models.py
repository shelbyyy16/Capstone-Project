from django.db import models
from enum import Enum  
from django.urls import reverse
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='group_members')

    def __str__(self):
        return self.name

class ExpenseType(Enum):
    LODGING = 'Lodging'
    FOOD = 'Food'
    BILL = 'Bill'
    TRANSPORTATION = 'Transportation'
    ENTERTAINMENT = 'Entertainment'
    PERSONAL = 'Personal'
    OTHER = 'Other'

class Expense(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    type = models.CharField(
        max_length=15,
        choices=[(tag.name, tag.value) for tag in ExpenseType],
        default=ExpenseType.LODGING.value
    )
    description = models.TextField(max_length=250, default='N/A')
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    divided_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.group.name} - Expense #{self.id}"