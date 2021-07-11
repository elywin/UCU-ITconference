# Generated by Django 3.2.4 on 2021-07-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_eventtitles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='faqs',
            name='answer',
        ),
        migrations.AddField(
            model_name='faqs',
            name='answer',
            field=models.ManyToManyField(to='events.Answer'),
        ),
    ]
