# Generated by Django 4.2.5 on 2023-12-03 04:41

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=128)),
                ('address_2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('state', localflavor.us.models.USStateField(default='NY', max_length=2)),
                ('zip_code', localflavor.us.models.USZipCodeField(blank=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
    ]