# Generated by Django 4.2.5 on 2024-01-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='card_details',
            field=models.BooleanField(default=False),
        ),
    ]