# Generated by Django 3.0.6 on 2020-05-29 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanji', '0006_auto_20200529_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grammarparticle',
            name='testing',
        ),
    ]