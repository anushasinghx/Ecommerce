# Generated by Django 5.0.7 on 2024-07-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_billingaddress_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='phone_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
