# Generated by Django 5.0.2 on 2024-02-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trilingo_app', '0002_remove_theme_name_theme_word_kz_theme_word_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='word_en',
            field=models.CharField(default='', max_length=35, verbose_name='Название темы на английском'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='word_ru',
            field=models.CharField(default='', max_length=35, verbose_name='Название темы на русском'),
        ),
    ]
