# Generated by Django 3.0.4 on 2020-03-18 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20200318_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favourites',
        ),
        migrations.RemoveField(
            model_name='user',
            name='recents',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
