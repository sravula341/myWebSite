# Generated by Django 3.1.2 on 2020-11-04 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0027_auto_20201104_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference_data_lookup',
            name='REC_EFFT_END_DT',
            field=models.DateField(verbose_name=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='reference_data_lookup',
            name='REC_EFFT_START_DT',
            field=models.DateField(verbose_name=datetime.datetime),
        ),
        migrations.DeleteModel(
            name='details',
        ),
    ]
