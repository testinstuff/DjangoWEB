# Generated by Django 3.0.6 on 2020-05-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanji', '0008_auto_20200529_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='grammarparticle',
            name='radical',
            field=models.CharField(default='', max_length=50),
        ),
    ]
