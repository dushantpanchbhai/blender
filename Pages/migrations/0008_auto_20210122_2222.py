# Generated by Django 3.1.4 on 2021-01-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0007_auto_20210111_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='index',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='index',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
