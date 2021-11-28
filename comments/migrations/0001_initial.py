# Generated by Django 3.2.7 on 2021-11-28 16:36

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Commentaire')),
                ('status', models.CharField(choices=[('ACTIVATED', 'Actif'), ('DELETED', 'Supprimé')], default='ACTIVATED', max_length=30, verbose_name='Statut')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication le')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')),
            ],
            options={
                'verbose_name_plural': 'comments',
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='CommentDelete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deletion_date', models.DateTimeField(auto_now=True, verbose_name='Suppression le')),
                ('deletion_reason', models.CharField(max_length=250, verbose_name='Raison de la suppression')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_comment', to='comments.comment')),
            ],
        ),
    ]
