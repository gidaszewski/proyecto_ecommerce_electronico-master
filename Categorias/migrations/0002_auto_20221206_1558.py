# Generated by Django 3.0.1 on 2022-12-06 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Categorias', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoriaProd',
            new_name='TCategorias',
        ),
        migrations.AlterModelOptions(
            name='tcategorias',
            options={'verbose_name': 'Tcategorias', 'verbose_name_plural': 'Tcategorias'},
        ),
    ]
