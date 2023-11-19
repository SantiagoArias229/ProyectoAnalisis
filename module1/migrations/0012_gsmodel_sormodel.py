# Generated by Django 4.2.4 on 2023-11-17 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0011_merge_20231116_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='gsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='sorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x0', models.TextField()),
                ('a', models.TextField()),
                ('b', models.TextField()),
                ('tol', models.FloatField()),
                ('niter', models.IntegerField()),
                ('w', models.FloatField()),
            ],
        ),
    ]