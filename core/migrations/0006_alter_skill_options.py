# Generated by Django 5.1.2 on 2024-11-08 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('order',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]
