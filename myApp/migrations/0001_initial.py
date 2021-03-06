# Generated by Django 3.1.1 on 2020-09-21 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courname', models.CharField(max_length=200)),
                ('instructorname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selfPaced', models.CharField(max_length=500)),
                ('instructorLed', models.CharField(max_length=500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.allcourses')),
            ],
        ),
    ]
