# Generated by Django 4.2.6 on 2023-11-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0017_remove_sormodel_a_alter_sormodel_b_alter_sormodel_x0_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sormodel',
            name='w',
            field=models.FloatField(null=True),
        ),
    ]
