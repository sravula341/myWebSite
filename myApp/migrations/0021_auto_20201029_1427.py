# Generated by Django 3.1.2 on 2020-10-29 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0020_auto_20201029_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='CITY',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='COUNTY',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='DEPARTMRNT',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='ECMROLES',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='MOBILEPHONENO',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='ORGANIZATION',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='STATE',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='STATUS',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='SUPERVISOR',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='USERTYPE',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='WORKPHONENO',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='ZIPCODE',
        ),
    ]
