# Generated by Django 3.1.4 on 2021-05-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0004_information_last_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='join',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='information',
            name='last_active',
            field=models.CharField(max_length=50),
        ),
    ]
