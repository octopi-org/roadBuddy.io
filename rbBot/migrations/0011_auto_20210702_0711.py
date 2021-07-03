# Generated by Django 3.2 on 2021-07-01 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbBot', '0010_user_routes_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='route',
            new_name='routes',
        ),
        migrations.AddField(
            model_name='user',
            name='planning_route',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]