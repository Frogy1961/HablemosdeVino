# Generated by Django 4.2.4 on 2023-09-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_post', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
