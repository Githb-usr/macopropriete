# Generated by Django 3.2.7 on 2021-11-15 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_auto_20211115_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photos',
            field=models.ManyToManyField(null=True, to='contents.Photo'),
        ),
    ]
