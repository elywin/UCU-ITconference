# Generated by Django 3.1.7 on 2021-07-04 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20210704_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='subquestions',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.faqs'),
        ),
        migrations.AlterField(
            model_name='subquestions',
            name='subquestion',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
