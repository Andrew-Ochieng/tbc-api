# Generated by Django 4.2.9 on 2024-01-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="updated_at",
            field=models.DateField(auto_now=True),
        ),
    ]
