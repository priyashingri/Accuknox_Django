from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal is running in the same database transaction.")
    else:
        print("Signal is NOT running in the same database transaction.")
