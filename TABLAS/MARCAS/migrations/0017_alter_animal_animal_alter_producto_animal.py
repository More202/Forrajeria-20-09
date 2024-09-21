# Generated by Django 5.1.1 on 2024-09-10 01:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MARCAS', '0016_alter_caja_abierta_alter_caja_fecha_hs_cier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animal',
            field=models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato'), ('Caballo', 'Caballo'), ('Aves', 'Aves'), ('Vaca', 'Vaca')], max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='MARCAS.animal'),
        ),
    ]
