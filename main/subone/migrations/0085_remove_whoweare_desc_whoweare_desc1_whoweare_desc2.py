# Generated by Django 5.0.6 on 2024-09-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subone', '0084_maincontactform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whoweare',
            name='desc',
        ),
        migrations.AddField(
            model_name='whoweare',
            name='desc1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='whoweare',
            name='desc2',
            field=models.TextField(blank=True, null=True),
        ),
    ]