# Generated by Django 3.2.7 on 2021-10-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20211022_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='A propos de moi'),
        ),
    ]
