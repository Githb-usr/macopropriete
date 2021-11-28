# Generated by Django 3.2.7 on 2021-11-28 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contentnews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsupdate',
            name='updater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_updater', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AddField(
            model_name='newsdelete',
            name='deleter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_deleter', to=settings.AUTH_USER_MODEL, verbose_name='Auteur de la suppression'),
        ),
        migrations.AddField(
            model_name='newsdelete',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_news', to='contentnews.news'),
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_news', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
    ]
