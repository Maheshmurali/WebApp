# Generated by Django 5.0 on 2024-01-04 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_generaldata_heart_dislikes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaldata',
            name='heart_Dislikes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='heart_Likes',
            field=models.IntegerField(null=True),
        ),
    ]
