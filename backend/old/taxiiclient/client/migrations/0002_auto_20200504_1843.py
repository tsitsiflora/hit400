# Generated by Django 2.2.12 on 2020-05-04 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('type', models.CharField(max_length=50)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
                ('pattern', models.CharField(max_length=100)),
                ('valid_from', models.DateTimeField()),
                ('labels', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
