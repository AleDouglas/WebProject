# Generated by Django 4.1.1 on 2022-09-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='BlogMedia', verbose_name='Thumbnail'),
        ),
    ]
