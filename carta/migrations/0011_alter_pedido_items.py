# Generated by Django 4.0.3 on 2024-05-28 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carta', '0010_auto_20240528_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='items', through='carta.PedidoItem', to='carta.item'),
        ),
    ]
