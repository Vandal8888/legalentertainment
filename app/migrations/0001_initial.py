# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('date', models.DateField(verbose_name='Дата')),
                ('html', models.TextField()),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('image', models.ImageField(upload_to='')),
                ('url', models.URLField(verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_ru', models.FileField(upload_to='', verbose_name='Файл (рус.)')),
                ('file_en', models.FileField(upload_to='', verbose_name='Файл (англ.)')),
                ('name', models.CharField(default='', max_length=128, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активно')),
                ('html', models.TextField()),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
    ]