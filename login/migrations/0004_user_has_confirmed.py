# Generated by Django 2.2 on 2019-06-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_confirmstring'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
