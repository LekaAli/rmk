# Generated by Django 2.0 on 2019-11-07 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_expense_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]