# Generated by Django 3.0.1 on 2022-12-06 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0009_auto_20221206_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundador',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 16, 2, 4, 460407)),
        ),
        migrations.AlterField(
            model_name='fundador',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 16, 2, 4, 460437)),
        ),
    ]
