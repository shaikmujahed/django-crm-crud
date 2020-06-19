from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save, pre_save
from .models import Customer


def customer_profile(sender, instance, **kwargs):
    group = Group.objects.get(name='customer')
    instance.groups.add(group)
    Customer.objects.create(user=instance, name=instance.username)
    print('User has been added')


post_save.connect(customer_profile, sender=User)
