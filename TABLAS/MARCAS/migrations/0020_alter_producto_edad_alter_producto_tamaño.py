# Generated by Django 5.1.1 on 2024-09-11 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MARCAS', '0019_alter_producto_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='edad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MARCAS.edad'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tamaño',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MARCAS.tamaño'),
        ),
    ]
