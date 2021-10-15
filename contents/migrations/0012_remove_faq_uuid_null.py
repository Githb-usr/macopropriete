# Generated by Django 3.2.7 on 2021-10-13 15:00
from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0011_populate_faq_uuid_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='exposed_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
