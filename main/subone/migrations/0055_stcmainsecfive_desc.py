# Generated by Django 5.0.6 on 2024-09-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subone', '0054_stcmainsecfour_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='stcmainsecfive',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
