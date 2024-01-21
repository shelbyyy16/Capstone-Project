# Generated by Django 5.0.1 on 2024-01-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_expense_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='expense',
            name='divided_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
