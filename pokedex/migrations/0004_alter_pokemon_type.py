# Generated by Django 4.2 on 2025-01-15 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('F', 'Fuego'), ('L', 'Lagartija'), ('E', 'Elèctrico'), ('A', 'Agua'), ('P', 'Planta'), ('T', 'Tierra')], max_length=30),
        ),
    ]
