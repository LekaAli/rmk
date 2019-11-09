# Generated by Django 2.0 on 2019-11-09 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20191109_0544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grossprofit',
            old_name='cost_of_sale',
            new_name='cost_of_sale_percentage',
        ),
        migrations.AddField(
            model_name='grossprofit',
            name='cost_of_sale_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]
