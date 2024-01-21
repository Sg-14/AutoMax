# Generated by Django 4.2.5 on 2023-12-03 18:07

from django.db import migrations, models
import django.db.models.deletion
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_photo'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='brand',
            field=models.CharField(choices=[('bmw', 'BMW'), ('mercedes benz', 'Mercedes Benz'), ('audi', 'Audi'), ('subaru', 'Subaru'), ('tesla', 'Tesla'), ('jaguar', 'Jaguar'), ('land rover', 'Land Rover'), ('bentley', 'Bentley'), ('bugatti', 'Bugatti'), ('ferrari', 'Ferrari'), ('lamborghini', 'Lamborghini'), ('honda', 'Honda'), ('toyota', 'Toyota'), ('chevrolet', 'Chevrolet'), ('porsche', 'Porsche')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listings',
            name='color',
            field=models.CharField(default='White', max_length=24),
        ),
        migrations.AddField(
            model_name='listings',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listings',
            name='engine',
            field=models.CharField(default='', max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listings',
            name='image',
            field=models.ImageField(default='', upload_to=main.utils.user_listing_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listings',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
        migrations.AddField(
            model_name='listings',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listings',
            name='model',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listings',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listings',
            name='vin',
            field=models.CharField(default='', max_length=17),
            preserve_default=False,
        ),
    ]
