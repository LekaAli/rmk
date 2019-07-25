# Generated by Django 2.1.4 on 2019-05-19 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates_video', models.ImageField(blank=True, default='date.png', upload_to='')),
                ('number_of_years_projected', models.FloatField(default=10)),
                ('year_end', models.DateField(blank=True, null=True)),
                ('year_start', models.DateField(blank=True, null=True)),
                ('previous_2_years_actuals_AFS', models.DateField(blank=True, null=True)),
                ('interim_management_accounts', models.DateField(blank=True, null=True)),
                ('Latest_signed_actuals_AFS', models.DateField(blank=True, null=True)),
                ('start_projection_date', models.DateField(blank=True, null=True)),
                ('month_1', models.DateField(blank=True, null=True)),
                ('month_2', models.DateField(blank=True, null=True)),
                ('month_3', models.DateField(blank=True, null=True)),
                ('month_4', models.DateField(blank=True, null=True)),
                ('month_5', models.DateField(blank=True, null=True)),
                ('month_6', models.DateField(blank=True, null=True)),
                ('month_7', models.DateField(blank=True, null=True)),
                ('month_8', models.DateField(blank=True, null=True)),
                ('month_9', models.DateField(blank=True, null=True)),
                ('month_10', models.DateField(blank=True, null=True)),
                ('month_11', models.DateField(blank=True, null=True)),
                ('month_12', models.DateField(blank=True, null=True)),
                ('month_13', models.DateField(blank=True, null=True)),
                ('month_14', models.DateField(blank=True, null=True)),
                ('month_15', models.DateField(blank=True, null=True)),
                ('month_16', models.DateField(blank=True, null=True)),
                ('month_17', models.DateField(blank=True, null=True)),
                ('month_18', models.DateField(blank=True, null=True)),
                ('month_19', models.DateField(blank=True, null=True)),
                ('month_20', models.DateField(blank=True, null=True)),
                ('month_21', models.DateField(blank=True, null=True)),
                ('month_22', models.DateField(blank=True, null=True)),
                ('month_23', models.DateField(blank=True, null=True)),
                ('month_24', models.DateField(blank=True, null=True)),
                ('month_25', models.DateField(blank=True, null=True)),
                ('month_26', models.DateField(blank=True, null=True)),
                ('month_27', models.DateField(blank=True, null=True)),
                ('month_28', models.DateField(blank=True, null=True)),
                ('month_29', models.DateField(blank=True, null=True)),
                ('month_30', models.DateField(blank=True, null=True)),
                ('month_31', models.DateField(blank=True, null=True)),
                ('month_32', models.DateField(blank=True, null=True)),
                ('month_33', models.DateField(blank=True, null=True)),
                ('month_34', models.DateField(blank=True, null=True)),
                ('month_35', models.DateField(blank=True, null=True)),
                ('month_36', models.DateField(blank=True, null=True)),
                ('year_1', models.DateField(blank=True, null=True)),
                ('year_2', models.DateField(blank=True, null=True)),
                ('year_3', models.DateField(blank=True, null=True)),
                ('year_4', models.DateField(blank=True, null=True)),
                ('year_5', models.DateField(blank=True, null=True)),
                ('year_6', models.DateField(blank=True, null=True)),
                ('year_7', models.DateField(blank=True, null=True)),
                ('year_8', models.DateField(blank=True, null=True)),
                ('year_9', models.DateField(blank=True, null=True)),
                ('year_10', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
