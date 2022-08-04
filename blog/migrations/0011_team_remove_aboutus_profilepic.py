# Generated by Django 4.0.5 on 2022-08-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('about', models.TextField()),
                ('profilepicture', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='profilePic',
        ),
    ]
