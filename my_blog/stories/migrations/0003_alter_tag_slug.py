# Generated by Django 4.2.5 on 2024-01-29 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
