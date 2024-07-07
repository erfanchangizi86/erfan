from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Product  # مدل خود را وارد کنید


@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
def clear_cache(sender, instance, **kwargs):
    cache.clear()
