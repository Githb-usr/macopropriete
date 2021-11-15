# Generated by Django 3.2.7 on 2021-11-15 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0008_alter_news_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photos',
            field=models.ManyToManyField(blank=True, to='contents.Photo'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='photos',
            field=models.ManyToManyField(blank=True, to='contents.Photo'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='photos',
            field=models.ManyToManyField(blank=True, to='contents.Photo'),
        ),
    ]
