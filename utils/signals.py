from django.db.models.signals import post_save
from django.dispatch import receiver
from revenues.models import ProductRevenue
from products.models import Sale


@receiver(post_save, sender=ProductRevenue)
def update_product_sale_revenue(sender, instance, created, **kwargs):
    Sale.objects.get(product_id=instance.product.id).save()
