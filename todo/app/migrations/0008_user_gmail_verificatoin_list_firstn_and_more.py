# Generated by Django 4.2 on 2023-06-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_user_gmail_verificatoin_list_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_gmail_verificatoin_list',
            name='firstn',
            field=models.CharField(default='suresh', max_length=200),
        ),
        migrations.AddField(
            model_name='user_gmail_verificatoin_list',
            name='lastn',
            field=models.CharField(default='peddimsetti', max_length=200),
        ),
        migrations.AddField(
            model_name='user_gmail_verificatoin_list',
            name='usern',
            field=models.CharField(default='suresh2988', max_length=200),
        ),
    ]
