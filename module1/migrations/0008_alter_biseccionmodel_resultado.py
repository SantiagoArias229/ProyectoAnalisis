# Generated by Django 4.2.4 on 2023-10-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0007_biseccionmodel_resultado_secantemodel_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biseccionmodel',
            name='resultado',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]