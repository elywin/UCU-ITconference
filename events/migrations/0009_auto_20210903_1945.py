# Generated by Django 3.2.4 on 2021-09-03 19:45

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_aboutus_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='picture',
            field=models.ImageField(blank=True, default='static/files/images/339c8096.jpg', null=True, upload_to='images/'),
        ),
    ]
