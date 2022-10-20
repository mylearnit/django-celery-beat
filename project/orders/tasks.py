from .models import Product, Order

from celery import shared_task
@shared_task
def db_check():
    obj,created = Product.objects.get_or_create(title='sugar')
    Order.objects.create(product=obj)
