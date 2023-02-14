# Generated by Django 3.2.10 on 2023-02-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleType', models.CharField(blank=True, max_length=50, null=True)),
                ('VehicleNumber', models.IntegerField(blank=True, null=True)),
                ('VehicleModel', models.CharField(blank=True, max_length=50, null=True)),
                ('VehicleDescription', models.CharField(blank=True, max_length=50, null=True)),
                ('Image', models.ImageField(upload_to='profile')),
            ],
        ),
    ]