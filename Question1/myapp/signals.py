import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("sending the Message.")
    time.sleep(5)  # time sleep for 5 sec
    print("Message sent successfully.")
