# Generated by Django 4.2.4 on 2023-11-17 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0014_gsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gsmodel',
            name='b',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
