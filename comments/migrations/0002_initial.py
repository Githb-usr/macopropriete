# Generated by Django 3.2.7 on 2021-12-10 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('contentnews', '0001_initial'),
        ('contentevent', '0001_initial'),
        ('incidents', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='commentdelete',
            name='deleter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_deleter', to=settings.AUTH_USER_MODEL, verbose_name='Auteur de la suppression'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_comments', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add_event_comment', to='contentevent.event'),
        ),
        migrations.AddField(
            model_name='comment',
            name='incident',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add_incident_comment', to='incidents.incident'),
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add_news_comment', to='contentnews.news'),
        ),
    ]
