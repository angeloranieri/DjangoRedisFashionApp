# Generated by Django 3.2.10 on 2022-08-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220728_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='nickname',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
