# Generated by Django 5.1.1 on 2024-09-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MARCAS', '0018_alter_animal_animal_alter_producto_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='peso',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
