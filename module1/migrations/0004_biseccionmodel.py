# Generated by Django 4.2.4 on 2023-10-22 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0003_remove_reglafalsamodel_error'),
    ]

    operations = [
        migrations.CreateModel(
            name='BiseccionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('func', models.CharField(max_length=255)),
                ('xi', models.FloatField()),
                ('xs', models.FloatField()),
                ('tol', models.FloatField()),
                ('iteraciones', models.IntegerField()),
            ],
        ),
    ]
