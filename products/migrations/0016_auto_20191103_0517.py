# Generated by Django 2.0 on 2019-11-03 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20191103_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profitbeforetax',
            name='expense',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='profitbeforetax',
            name='gross',
            field=models.FloatField(default=0.0),
        ),
    ]