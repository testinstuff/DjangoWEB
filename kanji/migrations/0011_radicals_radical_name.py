# Generated by Django 3.0.6 on 2020-05-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanji', '0010_radicals'),
    ]

    operations = [
        migrations.AddField(
            model_name='radicals',
            name='radical_name',
            field=models.CharField(default='', max_length=25),
        ),
    ]
