# Generated by Django 2.0 on 2019-11-12 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_productseasonalityrampup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productseasonalityrampup',
            name='rampup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rampup_value', to='rampup.RampUpValue'),
        ),
        migrations.AlterField(
            model_name='productseasonalityrampup',
            name='seasonality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seasonality_value', to='seasonality.SeasonalityValue'),
        ),
    ]
