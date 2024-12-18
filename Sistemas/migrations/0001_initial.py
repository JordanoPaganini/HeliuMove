# Generated by Django 5.0.7 on 2024-08-10 23:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sistemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=5)),
                ('voltage', models.CharField(max_length=5)),
                ('current', models.CharField(max_length=5)),
                ('datatime', models.DateTimeField()),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistemas.sistemas')),
            ],
        ),
    ]
