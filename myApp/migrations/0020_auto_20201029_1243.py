# Generated by Django 3.1.2 on 2020-10-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0019_auto_20201028_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='CITY',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='COUNTY',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='DEPARTMRNT',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='ECMROLES',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='MOBILEPHONENO',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='ORGANIZATION',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='STATE',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='STATUS',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='SUPERVISOR',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='USERTYPE',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='WORKPHONENO',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='ZIPCODE',
            field=models.CharField(default='', max_length=200),
        ),
    ]