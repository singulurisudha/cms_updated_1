# Generated by Django 5.0.1 on 2024-02-02 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='category',
        ),
    ]
