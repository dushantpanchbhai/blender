# Generated by Django 3.1.4 on 2021-01-10 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0005_auto_20210110_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='link',
            field=models.URLField(max_length=50),
        ),
    ]