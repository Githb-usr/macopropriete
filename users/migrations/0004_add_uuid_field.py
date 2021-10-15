# Generated by Django 3.2.7 on 2021-10-13 09:07
from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='exposed_id',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Pending', 'En attente'), ('Validated', 'Validé')], default='Pending', max_length=15, verbose_name='Statut'),
        ),
    ]