# Generated by Django 5.0.4 on 2024-07-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_disc_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='disc',
            name='country',
            field=models.CharField(default='null', max_length=255, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='disc',
            name='image_url_2',
            field=models.URLField(default='null', verbose_name='Image URL'),
        ),
        migrations.AddField(
            model_name='disc',
            name='image_url_3',
            field=models.URLField(default='null', verbose_name='Image URL'),
        ),
        migrations.AddField(
            model_name='disc',
            name='style',
            field=models.CharField(default='null', max_length=255, verbose_name='Style'),
        ),
    ]
