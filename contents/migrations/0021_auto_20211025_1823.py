# Generated by Django 3.2.7 on 2021-10-25 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0020_auto_20211022_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('CONDOMINIUM', 'Copropriété'), ('MEETING', 'Réunion'), ('PARTY', 'Fête'), ('WEBSITE', 'Site'), ('WORKS', 'Travaux'), ('MISCELLANEOUS', 'Divers')], default='MISCELLANEOUS', max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('CONDOMINIUM', 'Copropriété'), ('WEBSITE', 'Le site'), ('MEETING', 'Réunion'), ('PARTY', 'Fête'), ('WORKS', 'Travaux'), ('MISCELLANEOUS', 'Divers')], default='MISCELLANEOUS', max_length=30),
        ),
    ]
