# Generated by Django 4.1.2 on 2022-12-03 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0003_alter_fundador_created_alter_fundador_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundador',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 12, 10, 42, 798049)),
        ),
        migrations.AlterField(
            model_name='fundador',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 12, 10, 42, 798049)),
        ),
    ]
