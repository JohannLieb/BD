# Generated by Django 2.0.4 on 2018-05-09 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0002_auto_20180509_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
