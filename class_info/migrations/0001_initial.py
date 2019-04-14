# Generated by Django 2.1.7 on 2019-04-14 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=20)),
                ('batch', models.CharField(max_length=20)),
                ('sem', models.IntegerField()),
                ('branch', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=20)),
                ('students', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('slot1', models.CharField(max_length=20)),
                ('slot2', models.CharField(max_length=20)),
                ('slot3', models.CharField(max_length=20)),
                ('slot4', models.CharField(max_length=20)),
                ('slot5', models.CharField(max_length=20)),
                ('slot6', models.CharField(max_length=20)),
                ('slot7', models.CharField(max_length=20)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_info.Classes')),
            ],
        ),
    ]
