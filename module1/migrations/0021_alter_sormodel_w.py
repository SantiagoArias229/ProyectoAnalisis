# Generated by Django 4.2.6 on 2023-11-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0020_lagrange_sormodel_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sormodel',
            name='w',
            field=models.FloatField(default=1),
        ),
    ]
