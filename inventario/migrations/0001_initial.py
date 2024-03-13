# Generated by Django 5.0.2 on 2024-03-11 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=30)),
                ('imagen_producto', models.CharField(max_length=30, null=True)),
                ('precio_producto', models.FloatField()),
                ('stock_producto', models.IntegerField(default=0)),
                ('origen_producto', models.CharField(max_length=30, null=True)),
                ('categoria_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.categorias')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
