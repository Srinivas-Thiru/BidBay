# Generated by Django 4.1.7 on 2023-04-08 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_categories_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
