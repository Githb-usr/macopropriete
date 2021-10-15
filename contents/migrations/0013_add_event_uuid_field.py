# Generated by Django 3.2.7 on 2021-10-13 15:05
from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0012_remove_faq_uuid_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='exposed_id',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]