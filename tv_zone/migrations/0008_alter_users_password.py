# Generated by Django 3.2.6 on 2021-08-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_zone', '0007_alter_users_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=10000),
        ),
    ]
