# Generated by Django 3.0.4 on 2020-03-18 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200318_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
