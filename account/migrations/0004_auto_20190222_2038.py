# Generated by Django 2.1.7 on 2019-02-23 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_user_favcolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateTimeField(null=True),
        ),
    ]