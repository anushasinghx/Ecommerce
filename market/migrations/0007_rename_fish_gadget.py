# Generated by Django 4.2.14 on 2024-10-15 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_category_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fish',
            new_name='Gadget',
        ),
    ]