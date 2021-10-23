# Generated by Django 3.2.7 on 2021-10-18 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0016_auto_20211017_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='contents'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='contents/events/'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='contents/faqs/'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='contents/incidents/'),
        ),
    ]