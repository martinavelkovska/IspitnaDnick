# Generated by Django 5.0.dev20230305130119 on 2023-06-05 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_kategorija_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategorija',
            name='user',
        ),
    ]
