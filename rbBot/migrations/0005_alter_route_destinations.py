# Generated by Django 3.2 on 2021-06-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbBot', '0004_auto_20210630_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='destinations',
            field=models.TextField(blank=True, default=None, max_length=4000, null=True),
        ),
    ]