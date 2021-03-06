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
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CONDOMINIUM', 'Copropriété'), ('MEETING', 'Réunion'), ('PARTY', 'Fête'), ('WEBSITE', 'Site'), ('WORKS', 'Travaux'), ('MISCELLANEOUS', 'Divers')], default='MISCELLANEOUS', max_length=30, verbose_name='Catégorie')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='News')),
                ('status', models.CharField(choices=[('ACTIVATED', 'Actif'), ('DELETED', 'Supprimé')], default='ACTIVATED', max_length=30, verbose_name='Statut')),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication le')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')),
            ],
            options={
                'verbose_name_plural': 'news',
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='NewsDelete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deletion_date', models.DateTimeField(auto_now=True, verbose_name='Suppression le')),
                ('deletion_reason', models.CharField(max_length=250, verbose_name='Raison de la suppression')),
            ],
        ),
        migrations.CreateModel(
            name='NewsUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Modification le')),
                ('update_reason', models.CharField(max_length=250, verbose_name='Raison de la modification')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_news', to='contentnews.news', verbose_name='News modifiée')),
            ],
        ),
    ]
