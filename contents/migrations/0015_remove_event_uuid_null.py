# Generated by Django 3.2.7 on 2021-10-13 15:06
from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0014_populate_event_uuid_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='exposed_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]