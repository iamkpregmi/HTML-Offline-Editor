# Generated by Django 5.0.1 on 2024-01-28 07:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myCKEditor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('html_data', ckeditor.fields.RichTextField()),
            ],
        ),
    ]