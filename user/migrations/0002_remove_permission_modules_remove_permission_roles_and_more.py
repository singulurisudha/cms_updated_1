# Generated by Django 4.2.5 on 2024-02-05 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='modules',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='role',
            name='users',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]