# Generated by Django 4.2.6 on 2023-11-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0025_alter_sormodel_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sormodel',
            name='error',
            field=models.IntegerField(blank=True),
        ),
    ]
