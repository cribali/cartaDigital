# Generated by Django 5.0.4 on 2024-04-18 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carta', '0002_categoria_alter_plato_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carta.clasificacion')),
            ],
        ),
    ]
