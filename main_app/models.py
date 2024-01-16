from django.db import models
from enum import Enum  
from django.urls import reverse

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30, unique=True)  
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class ExpenseType(Enum):
    LODGING = 'Lodging'
    FOOD = 'Food'
    BILL = 'Bill'
    TRANSPORTATION = 'Transportation'
    ENTERTAINMENT = 'Entertainment'

class Expense(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    type = models.CharField(
        max_length=15,
        choices=[(tag.name, tag.value) for tag in ExpenseType],
        default=ExpenseType.LODGING.value
    )
    description = models.TextField(max_length=250, default='N/A')
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.group.name} - Expense #{self.id}"