# Generated by Django 2.0 on 2019-09-08 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190908_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]