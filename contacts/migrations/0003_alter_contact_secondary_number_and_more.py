# Generated by Django 4.2.1 on 2023-07-21 11:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='secondary_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='contact',
            name='twitter_username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
