# Generated by Django 3.2.16 on 2023-03-03 02:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='video/')),
                ('processing', models.BooleanField(default=False)),
                ('processing_success', models.BooleanField(blank=True, default=None, null=True)),
            ],
        ),
    ]
