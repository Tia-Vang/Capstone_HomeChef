# Generated by Django 4.0.2 on 2022-05-11 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homechefapp', '0009_delete_comment_section_delete_recipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 11, 10, 49, 42, 87442)),
        ),
    ]