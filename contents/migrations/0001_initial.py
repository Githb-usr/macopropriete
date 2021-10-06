# Generated by Django 3.2.7 on 2021-10-06 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='contents/articles/')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name="Création de l'article")),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'articles',
            },
        ),
        migrations.CreateModel(
            name='ArticleDelete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_date', models.DateTimeField(auto_now=True, null=True)),
                ('delete_reason', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('update_reason', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Création du commentaire')),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
                ('status', models.CharField(max_length=30)),
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
                ('delete_date', models.DateTimeField(auto_now=True, null=True)),
                ('delete_reason', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='contents/events/')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name="Création de l'évènement")),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
                ('start_date', models.DateTimeField(auto_now=True, verbose_name="Début de l'évènement")),
                ('end_date', models.DateTimeField(auto_now=True, verbose_name="Fin de l'évènement")),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventDelete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_date', models.DateTimeField(auto_now=True, null=True)),
                ('delete_reason', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='EventUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('update_reason', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_section', models.CharField(max_length=30)),
                ('question', models.CharField(max_length=250)),
                ('answer', models.TextField()),
                ('image', models.ImageField(upload_to='contents/faqs/')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Création de la question')),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Faqs',
            },
        ),
        migrations.CreateModel(
            name='FaqDelete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_date', models.DateTimeField(auto_now=True, null=True)),
                ('delete_reason', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='FaqUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('update_reason', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_type', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='contents/incidents/')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name="Création de l'incident")),
            ],
            options={
                'verbose_name_plural': 'incidents',
            },
        ),
        migrations.CreateModel(
            name='IncidentDelete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_date', models.DateTimeField(auto_now=True, null=True)),
                ('delete_reason', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='IncidentTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'en attente'), ('Rejected', 'rejeté'), ('Registered', 'enregistré'), ('In progress', 'en cours'), ('Closed', 'fermé')], max_length=20)),
                ('status_date', models.DateTimeField(auto_now=True)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incident', to='contents.incident')),
            ],
            options={
                'verbose_name_plural': 'status',
            },
        ),
    ]
