# Generated by Django 4.2.4 on 2023-11-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0027_merge_20231119_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='newtonint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('pol', models.CharField(max_length=2000)),
            ],
        ),
    ]
