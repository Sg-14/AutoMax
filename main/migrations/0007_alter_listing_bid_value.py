# Generated by Django 4.2.5 on 2024-01-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_listing_bid_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bid_value',
            field=models.CharField(default=100, max_length=100),
        ),
    ]
