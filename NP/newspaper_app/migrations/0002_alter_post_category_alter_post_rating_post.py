# Generated by Django 4.2.5 on 2023-11-06 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='posts', through='newspaper_app.PostCategory', to='newspaper_app.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating_post',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
