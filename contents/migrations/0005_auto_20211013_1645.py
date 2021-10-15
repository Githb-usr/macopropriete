# Generated by Django 3.2.7 on 2021-10-13 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contents', '0004_auto_20211013_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='faq_section',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='incident_type',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Condominium', 'Copropriété'), ('Meeting', 'Réunion'), ('Website', 'Site'), ('Works', 'Travaux'), ('Miscellaneous', 'Divers')], default='Miscellaneous', max_length=30),
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Party', 'Fête'), ('Website', 'Site'), ('Meeting', 'Réunion'), ('Works', 'Travaux'), ('Miscellaneous', 'Divers')], default='Miscellaneous', max_length=30),
        ),
        migrations.AddField(
            model_name='faq',
            name='category',
            field=models.CharField(choices=[('Buildings', 'Les bâtiments'), ('Individual garages', 'Les garages'), ('Park', 'Le parc'), ('Car parks', 'Les parkings'), ('Miscellaneous', 'Divers')], default='Miscellaneous', max_length=30),
        ),
        migrations.AddField(
            model_name='incident',
            name='category',
            field=models.CharField(choices=[('Accident', 'Accident'), ('Damage', 'Dégradation'), ('Water leakage', "Fuite d'eau"), ('Breakdown', 'Panne'), ('Miscellaneous', 'Divers')], default='Miscellaneous', max_length=30, verbose_name="Type d'incident"),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_article', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Activated', 'Actif'), ('Deleted', 'Supprimé')], default='Activated', max_length=30),
        ),
        migrations.AlterField(
            model_name='articledelete',
            name='deleter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_deleter', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='articleupdate',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Date de la modification'),
        ),
        migrations.AlterField(
            model_name='articleupdate',
            name='update_reason',
            field=models.CharField(max_length=250, verbose_name='Motif de la modification'),
        ),
        migrations.AlterField(
            model_name='articleupdate',
            name='updater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_updater', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_comments', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('Activated', 'Actif'), ('Deleted', 'Supprimé')], default='Activated', max_length=30),
        ),
        migrations.AlterField(
            model_name='commentdelete',
            name='delete_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Date de suppression'),
        ),
        migrations.AlterField(
            model_name='commentdelete',
            name='delete_reason',
            field=models.CharField(max_length=250, verbose_name='Motif de la suppression'),
        ),
        migrations.AlterField(
            model_name='commentdelete',
            name='deleter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_deleter', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='event',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_events', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='event',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Publication de l'évènement"),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Activated', 'Actif'), ('Deleted', 'Supprimé')], default='Activated', max_length=30),
        ),
        migrations.AlterField(
            model_name='eventdelete',
            name='delete_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Date de suppression'),
        ),
        migrations.AlterField(
            model_name='eventdelete',
            name='delete_reason',
            field=models.CharField(max_length=250, verbose_name='Motif de la suppression'),
        ),
        migrations.AlterField(
            model_name='eventdelete',
            name='deleter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_deleter', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='eventupdate',
            name='updater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_updater', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_faq', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Publication de la question'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='status',
            field=models.CharField(choices=[('Activated', 'Actif'), ('Deleted', 'Supprimé')], default='Activated', max_length=30),
        ),
        migrations.AlterField(
            model_name='faqdelete',
            name='deleter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_deleter', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='faqupdate',
            name='updater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_updater', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_incident', to=settings.AUTH_USER_MODEL, verbose_name='Déclarant'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Publication de l'incident"),
        ),
        migrations.AlterField(
            model_name='incidentdelete',
            name='delete_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Date de suppression'),
        ),
        migrations.AlterField(
            model_name='incidentdelete',
            name='delete_reason',
            field=models.CharField(max_length=250, verbose_name='Motif de la suppression'),
        ),
        migrations.AlterField(
            model_name='incidentdelete',
            name='deleter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incident_deleter', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='incidenttracking',
            name='status',
            field=models.CharField(choices=[('Pending', 'en attente'), ('Rejected', 'rejeté'), ('Registered', 'enregistré'), ('In progress', 'en cours'), ('Closed', 'fermé')], default='Pending', max_length=20),
        ),
    ]