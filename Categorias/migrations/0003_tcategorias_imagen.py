# Generated by Django 3.0.1 on 2022-12-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categorias', '0002_auto_20221206_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='tcategorias',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='categorias'),
        ),
    ]
