# Generated by Django 4.2.4 on 2023-11-20 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0029_rename_newtonint_newtonintmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtonintmodel',
            name='pol',
            field=models.TextField(max_length=2000),
        ),
    ]
