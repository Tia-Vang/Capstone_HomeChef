# Generated by Django 4.0.2 on 2022-05-11 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homechefapp', '0012_alter_comment_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 11, 14, 1, 35, 659074)),
        ),
    ]