# Generated by Django 3.1.2 on 2020-11-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0031_auto_20201104_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference_data_lookup',
            name='REC_EFFT_END_DT',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reference_data_lookup',
            name='REC_EFFT_START_DT',
            field=models.DateField(),
        ),
    ]
