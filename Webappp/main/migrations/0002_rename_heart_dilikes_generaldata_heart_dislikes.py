# Generated by Django 5.0 on 2024-01-03 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generaldata',
            old_name='heart_Dilikes',
            new_name='heart_Dislikes',
        ),
    ]