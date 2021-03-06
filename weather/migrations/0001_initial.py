# Generated by Django 2.0 on 2019-02-27 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaxTemperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0.0)),
                ('region', models.CharField(choices=[('UK', 'UK'), ('England', 'England'), ('Scotland', 'Scotland'), ('Wales', 'Wales')], max_length=8)),
                ('record_date', models.DateField()),
            ],
            options={
                'ordering': ['record_date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MinTemperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0.0)),
                ('region', models.CharField(choices=[('UK', 'UK'), ('England', 'England'), ('Scotland', 'Scotland'), ('Wales', 'Wales')], max_length=8)),
                ('record_date', models.DateField()),
            ],
            options={
                'ordering': ['record_date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rainfall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0.0)),
                ('region', models.CharField(choices=[('UK', 'UK'), ('England', 'England'), ('Scotland', 'Scotland'), ('Wales', 'Wales')], max_length=8)),
                ('record_date', models.DateField()),
            ],
            options={
                'ordering': ['record_date'],
                'abstract': False,
            },
        ),
    ]
