# Generated by Django 3.2.6 on 2021-08-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_zone', '0004_alter_users_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=75, unique=True),
        ),
    ]