# Generated by Django 4.0.6 on 2022-07-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_record_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
