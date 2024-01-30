# Generated by Django 4.2.5 on 2024-01-29 22:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_alter_category_slug_alter_stories_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='stories',
            name='slug',
            field=models.SlugField(max_length=255, validators=[django.core.validators.MinLengthValidator(5, message='Минимум 5 символов'), django.core.validators.MaxLengthValidator(100, message='Максимум 100 символов')], verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]