# Generated by Django 3.2.7 on 2021-12-10 21:47

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CONDOMINIUM', 'Copropriété'), ('WEBSITE', 'Le site'), ('MEETING', 'Réunion'), ('PARTY', 'Fête'), ('WORKS', 'Travaux'), ('MISCELLANEOUS', 'Divers')], default='MISCELLANEOUS', max_length=30, verbose_name='Catégorie')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Evènement')),
                ('start_date', models.DateTimeField(verbose_name="Début de l'évènement")),
                ('end_date', models.DateTimeField(verbose_name="Fin de l'évènement")),
                ('status', models.CharField(choices=[('ACTIVATED', 'Actif'), ('DELETED', 'Supprimé')], default='ACTIVATED', max_length=30, verbose_name='Statut')),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication le')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventDelete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deletion_date', models.DateTimeField(auto_now=True, verbose_name='Suppression le')),
                ('deletion_reason', models.CharField(max_length=250, verbose_name='Raison de la suppression')),
            ],
        ),
        migrations.CreateModel(
            name='EventUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Modification le')),
                ('update_reason', models.CharField(max_length=250, verbose_name='Raison de la modification')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_event', to='contentevent.event')),
            ],
        ),
    ]
