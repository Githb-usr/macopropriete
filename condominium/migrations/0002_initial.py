# Generated by Django 3.2.7 on 2021-11-28 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('condominium', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ownership',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lot_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lot',
            name='condominium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lot_condominium', to='condominium.condominium'),
        ),
        migrations.AddField(
            model_name='entrance',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building_of_entrance', to='condominium.building'),
        ),
        migrations.AddField(
            model_name='cellar',
            name='entrance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrance_cellar', to='condominium.entrance'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='entrance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrance_apartment', to='condominium.entrance'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='parking_space_zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parking_space_zone', to='condominium.zone'),
        ),
    ]
