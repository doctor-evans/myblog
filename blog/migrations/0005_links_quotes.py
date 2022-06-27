# Generated by Django 4.0.5 on 2022-06-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.CharField(max_length=80)),
                ('facebook', models.CharField(max_length=80)),
                ('youtube', models.CharField(max_length=80)),
                ('instagram', models.CharField(max_length=80)),
                ('linkedin', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=250)),
            ],
        ),
    ]
