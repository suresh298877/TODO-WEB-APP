# Generated by Django 4.2 on 2023-06-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user_gmail_verificatoin_list_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_gmail_verificatoin_list',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_gmail_verificatoin_list',
            name='email',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
