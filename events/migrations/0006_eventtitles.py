# Generated by Django 3.2.4 on 2021-07-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_faqs_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
            ],
        ),
    ]
