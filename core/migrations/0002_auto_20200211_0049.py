# Generated by Django 3.0.3 on 2020-02-11 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=20),
        ),
    ]
