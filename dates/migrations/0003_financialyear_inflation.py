# Generated by Django 2.0 on 2019-10-31 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0002_financialyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialyear',
            name='inflation',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]