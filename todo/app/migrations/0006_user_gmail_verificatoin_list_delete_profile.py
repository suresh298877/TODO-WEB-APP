# Generated by Django 4.2 on 2023-06-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_gmail_verificatoin_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
