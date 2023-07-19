from django.db import models
from django.contrib.auth.models import User
# from.forms import SignUpForm
# Create your models here.
class TODO(models.Model):
    status_choices=[
        ('C','COMPLETED'),
        ('P','PENDING'),
    ]
    priority_choices=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
    ]
    title=models.CharField(max_length=200)
    status=models.CharField(max_length=2,choices=status_choices)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=2,choices=priority_choices)


class user_gmail_verificatoin_list(models.Model):
    email=models.CharField(max_length=200,primary_key=True)
    password=models.CharField(max_length=200)
    token=models.CharField(max_length=200)
    firstn=models.CharField(max_length=200,default='suresh')
    lastn=models.CharField(max_length=200,default='peddimsetti')
    usern=models.CharField(max_length=200,default='suresh2988')

    

# class Profile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     email_token=models.CharField(max_length=200)
#     is_verified=models.BooleanField(default=False)