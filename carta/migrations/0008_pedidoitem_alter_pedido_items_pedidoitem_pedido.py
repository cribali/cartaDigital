# Generated by Django 4.0.3 on 2024-05-28 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carta', '0007_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_seleccionada', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carta.item')),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='items',
            field=models.ManyToManyField(through='carta.PedidoItem', to='carta.item'),
        ),
        migrations.AddField(
            model_name='pedidoitem',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carta.pedido'),
        ),
    ]
