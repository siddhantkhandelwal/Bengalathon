# Generated by Django 2.1.4 on 2019-01-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190102_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='claim_flag',
            field=models.BooleanField(default=False),
        ),
    ]