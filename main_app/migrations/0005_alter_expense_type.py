# Generated by Django 5.0.1 on 2024-01-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_expense_divided_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='type',
            field=models.CharField(choices=[('LODGING', 'Lodging'), ('FOOD', 'Food'), ('BILL', 'Bill'), ('TRANSPORTATION', 'Transportation'), ('ENTERTAINMENT', 'Entertainment'), ('PERSONAL', 'Personal'), ('OTHER', 'Other')], default='Lodging', max_length=15),
        ),
    ]
