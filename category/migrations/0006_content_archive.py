# Generated by Django 5.0.1 on 2024-02-09 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_alter_category_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
