# Generated by Django 5.1.2 on 2024-11-09 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='name',
        ),
    ]
