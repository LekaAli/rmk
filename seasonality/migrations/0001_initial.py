# Generated by Django 2.1.4 on 2019-05-19 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSeasonality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seasonality_description', models.CharField(max_length=50)),
                ('month_1_seasonality', models.FloatField(default=0.083)),
                ('month_2_seasonality', models.FloatField(default=0.083)),
                ('month_3_seasonality', models.FloatField(default=0.083)),
                ('month_4_seasonality', models.FloatField(default=0.083)),
                ('month_5_seasonality', models.FloatField(default=0.083)),
                ('month_6_seasonality', models.FloatField(default=0.083)),
                ('month_7_seasonality', models.FloatField(default=0.083)),
                ('month_8_seasonality', models.FloatField(default=0.083)),
                ('month_9_seasonality', models.FloatField(default=0.083)),
                ('month_10_seasonality', models.FloatField(default=0.083)),
                ('month_11_seasonality', models.FloatField(default=0.083)),
                ('month_12_seasonality', models.FloatField(default=0.083)),
            ],
        ),
    ]
