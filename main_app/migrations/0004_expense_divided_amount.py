# Generated by Django 5.0.1 on 2024-01-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_group_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='divided_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]