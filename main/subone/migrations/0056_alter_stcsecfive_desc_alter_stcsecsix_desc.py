# Generated by Django 5.0.6 on 2024-09-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subone', '0055_stcmainsecfive_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stcsecfive',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stcsecsix',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
