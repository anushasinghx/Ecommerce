# Generated by Django 4.2.14 on 2024-09-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_remove_order_ordered_items_order_ordered_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
