# Generated by Django 4.2.4 on 2023-10-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0006_rename_tol_secantemodel_tol_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='biseccionmodel',
            name='resultado',
            field=models.CharField(default='nothing', max_length=300),
        ),
        migrations.AddField(
            model_name='secantemodel',
            name='error',
            field=models.IntegerField(default=2),
        ),
    ]
