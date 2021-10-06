# Generated by Django 3.2.7 on 2021-10-06 07:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Adresse email')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Pseudonyme')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Inscription')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Dernière connexion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
                ('user_type', models.CharField(choices=[('Owner occupier', 'Copropriétaire occupant'), ('Owner lessor', 'Copropriétaire bailleur'), ('Tenant', 'Locataire'), ('Syndic', 'Syndic')], max_length=20)),       
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Prénom')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nom')),
                ('contact_email', models.EmailField(max_length=255, verbose_name='Adresse email de contact')),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Téléphone')),
                ('avatar', models.ImageField(upload_to='users/avatars/')),
                ('about', models.TextField(blank=True, null=True)),
                ('is_resident', models.BooleanField(default=True)),
                ('is_union_council', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('-date_joined', '-updated_at'),
            },
        ),
    ]
