# Generated by Django 4.2.4 on 2023-09-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
    ]
