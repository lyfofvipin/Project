# Generated by Django 2.1.7 on 2019-02-26 18:04

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_auto_20190224_1742'),
        ('Demo', '0011_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_student', models.BooleanField(default=False, verbose_name='student status')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='teacher status')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
