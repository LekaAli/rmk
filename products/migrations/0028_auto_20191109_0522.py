# Generated by Django 2.0 on 2019-11-09 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_remove_sale_financial_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='monthly_sale',
            new_name='month_sale',
        ),
    ]
