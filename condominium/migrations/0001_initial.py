# Generated by Django 3.2.7 on 2021-10-06 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condominium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condominium_type', models.CharField(choices=[('Building', 'Immeuble'), ('Individual garages', 'Garages'), ('Park', 'Parc')], max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('share', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='condominium/condominium/')),
            ],
            options={
                'verbose_name_plural': 'condominiums',
            },
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_type', models.CharField(choices=[('Apartment', 'Appartement'), ('Cellar', 'Cave'), ('Individual garage', 'Garage')], max_length=20)),
                ('number', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('share', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='condominium/lot/')),
            ],
            options={
                'verbose_name_plural': 'lots',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='condominium/zone/')),
            ],
            options={
                'verbose_name_plural': 'zones',
            },
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acquisition_date', models.DateTimeField(blank=True, null=True)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_lot', to='condominium.lot')),
            ],
        ),
    ]
