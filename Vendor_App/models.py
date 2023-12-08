from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count, Avg
# vendor_app/models.py
from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True, primary_key=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True, primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    # quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    if instance.status == 'completed':
        # Update On-Time Delivery Rate
        completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
        on_time_delivery_rate = completed_orders.filter(delivery_date__lte=instance.delivery_date).count() / completed_orders.count()
        instance.vendor.on_time_delivery_rate = on_time_delivery_rate if on_time_delivery_rate else 0

        # Update Quality Rating Average
        completed_orders_with_rating = completed_orders.exclude(quality_rating__isnull=True)
        quality_rating_avg = completed_orders_with_rating.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0
        instance.vendor.quality_rating_avg = quality_rating_avg if quality_rating_avg else 0

        instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_response_time(sender, instance, **kwargs):
    if instance.acknowledgment_date:
        # Update Average Response Time
        response_times = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).values_list('acknowledgment_date', 'issue_date')
        average_response_time = sum((ack_date - issue_date).total_seconds() for ack_date, issue_date in response_times) / len(response_times)
        instance.vendor.average_response_time = average_response_time
        instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, **kwargs):
    # Update Fulfillment Rate
    fulfilled_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed', quality_rating__isnull=False)
    fulfillment_rate = fulfilled_orders.count() / PurchaseOrder.objects.filter(vendor=instance.vendor).count()
    instance.vendor.fulfillment_rate = fulfillment_rate
    instance.vendor.save()


