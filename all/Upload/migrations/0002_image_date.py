# Generated by Django 2.0.3 on 2018-03-19 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
