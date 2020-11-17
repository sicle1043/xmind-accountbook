# Generated by Django 3.1.2 on 2020-11-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('type', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
            ],
        ),
    ]
