# Generated by Django 4.1.1 on 2022-09-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default=None, upload_to='', verbose_name='Thumbnail'),
            preserve_default=False,
        ),
    ]