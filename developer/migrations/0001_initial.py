# Generated by Django 4.2.7 on 2023-11-10 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='dev_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile/developer/')),
                ('headline', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=255)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('experience', models.CharField(max_length=200)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('qualification', models.CharField(max_length=255)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('media_links', models.URLField(blank=True)),
                ('skills', models.ManyToManyField(to='developer.skill')),
            ],
        ),
    ]