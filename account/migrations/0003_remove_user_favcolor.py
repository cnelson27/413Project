# Generated by Django 2.1.7 on 2019-02-22 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_favcolor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favcolor',
        ),
    ]
