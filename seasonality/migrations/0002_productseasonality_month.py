# Generated by Django 2.0 on 2019-09-07 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasonality', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productseasonality',
            name='month',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
