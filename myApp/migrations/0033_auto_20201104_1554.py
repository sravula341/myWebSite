# Generated by Django 3.1.2 on 2020-11-04 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0032_auto_20201104_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference_data_lookup',
            name='REC_EFFT_END_DT',
            field=models.DateField(verbose_name=datetime.datetime(2020, 11, 4, 15, 54, 10, 247899)),
        ),
        migrations.AlterField(
            model_name='reference_data_lookup',
            name='REC_EFFT_START_DT',
            field=models.DateField(verbose_name=datetime.datetime(2020, 11, 4, 15, 54, 10, 247899)),
        ),
    ]