# Generated by Django 2.2.1 on 2019-05-23 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Title',
            field=models.CharField(default='Title Of Post', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='Auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='Content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='Publish_date',
            field=models.DateTimeField(),
        ),
    ]