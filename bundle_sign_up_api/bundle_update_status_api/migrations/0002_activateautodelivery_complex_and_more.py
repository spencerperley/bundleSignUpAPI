# Generated by Django 5.0 on 2023-12-26 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bundle_update_status_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activateautodelivery',
            name='complex',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='activateautodelivery',
            name='firstName',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='activateautodelivery',
            name='lastName',
            field=models.CharField(max_length=255),
        ),
    ]
