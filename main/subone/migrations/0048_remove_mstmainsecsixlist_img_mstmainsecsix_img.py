# Generated by Django 5.0.6 on 2024-09-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subone', '0047_mstmainmetatag_mstmainsecfivelist_mstmainsecfourlist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mstmainsecsixlist',
            name='img',
        ),
        migrations.AddField(
            model_name='mstmainsecsix',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
