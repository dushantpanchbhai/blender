# Generated by Django 3.1.4 on 2021-05-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0003_information_join'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='last_active',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]