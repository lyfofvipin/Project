# Generated by Django 2.1.7 on 2019-02-27 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0019_remove_buyer_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='User',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
    ]
