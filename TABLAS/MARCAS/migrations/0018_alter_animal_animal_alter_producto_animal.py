# Generated by Django 5.1.1 on 2024-09-10 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MARCAS', '0017_alter_animal_animal_alter_producto_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animal',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MARCAS.animal'),
        ),
    ]
