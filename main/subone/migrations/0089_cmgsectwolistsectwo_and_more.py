# Generated by Django 5.0.6 on 2024-09-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subone', '0088_cmgsectwolist_img_alter_cmgsectwo_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CmgSecTwoListSecTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='CmgSecTwoList',
            new_name='CmgSecTwoListSecOne',
        ),
        migrations.RemoveField(
            model_name='cmgsectwo',
            name='cmg_sec_two_list',
        ),
        migrations.AddField(
            model_name='cmgsectwo',
            name='cmg_sec_two_list_sec_one',
            field=models.ManyToManyField(blank=True, null=True, related_name='cmg_sec_two_list_sec_one', to='subone.cmgsectwolistsecone'),
        ),
        migrations.AddField(
            model_name='cmgsectwo',
            name='cmg_sec_two_list_sec_two',
            field=models.ManyToManyField(blank=True, null=True, related_name='cmg_sec_two_list_sec_two', to='subone.cmgsectwolistsectwo'),
        ),
    ]