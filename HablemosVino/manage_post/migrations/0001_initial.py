# Generated by Django 4.2.4 on 2023-08-08 23:17

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('introduction', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='Articles')),
                ('body', ckeditor.fields.RichTextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='Categories')),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('featured', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_post.article')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
