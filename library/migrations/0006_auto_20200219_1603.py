# Generated by Django 2.2 on 2020-02-19 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20200219_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='height',
        ),
        migrations.RemoveField(
            model_name='book',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='book',
            name='width',
        ),
    ]
