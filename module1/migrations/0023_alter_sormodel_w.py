# Generated by Django 4.2.6 on 2023-11-19 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0022_alter_sormodel_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sormodel',
            name='w',
            field=models.FloatField(default=0),
        ),
    ]
