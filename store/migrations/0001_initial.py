# Generated by Django 5.0.4 on 2024-07-11 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=255, verbose_name='Artist')),
                ('album', models.CharField(max_length=255, verbose_name='Album')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('record_label', models.CharField(max_length=255, verbose_name='Record Label')),
                ('code', models.CharField(max_length=255, verbose_name='Code')),
                ('disc_condition', models.CharField(max_length=255, verbose_name='Disc Condition')),
                ('cover_condition', models.CharField(max_length=255, verbose_name='Cover Condition')),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('stock', models.IntegerField(default=1, verbose_name='Stock')),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
            options={
                'verbose_name': 'Disc',
                'verbose_name_plural': 'Disc',
            },
        ),
    ]
