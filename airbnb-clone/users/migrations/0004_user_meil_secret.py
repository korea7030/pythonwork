# Generated by Django 2.2.5 on 2020-03-18 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200318_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='meil_secret',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
