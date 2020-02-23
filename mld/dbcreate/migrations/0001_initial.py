# Generated by Django 3.0.3 on 2020-02-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlgorithmsBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algo_name', models.CharField(max_length=50, unique=True)),
                ('algo_desc', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='DatasetsBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_name', models.CharField(max_length=50, unique=True)),
                ('dataset_desc', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='MetricsBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_name', models.CharField(max_length=50, unique=True)),
                ('metric_desc', models.CharField(max_length=512)),
            ],
        ),
    ]
