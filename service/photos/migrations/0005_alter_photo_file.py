# Generated by Django 3.2.16 on 2023-03-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_photo_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
