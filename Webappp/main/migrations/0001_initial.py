# Generated by Django 5.0 on 2024-01-03 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generaldata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_Likes', models.IntegerField(null=True)),
                ('heart_Dilikes', models.IntegerField(null=True)),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
    ]