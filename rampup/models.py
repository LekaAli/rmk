from django.db import models
from django.urls import reverse


class ProductRampUp(models.Model):
    description = models.CharField(max_length=75, blank=True, null=True)
    product = models.ForeignKey('products.Product', related_name='product_rampup', on_delete=models.CASCADE, blank=True, null=True)
    percentage = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product RampUp'
        verbose_name_plural = 'Product RampUp'

    def save(self, *args, **kwargs):

        super(ProductRampUp, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')

    def __str__(self):
        return '%s: %s' % (self.description, self.percentage)
