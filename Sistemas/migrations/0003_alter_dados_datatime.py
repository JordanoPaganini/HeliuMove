# Generated by Django 5.0.7 on 2024-08-10 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistemas', '0002_alter_dados_datatime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='datatime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
