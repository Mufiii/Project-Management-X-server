# Generated by Django 4.2.7 on 2023-12-01 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='field',
            new_name='field_of_study',
        ),
    ]