from django.db import models
from users.models import CustomUser
from simple_carpet.models import Carpet


# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    finger_print = models.CharField(max_length=255, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=18, decimal_places=2)


class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    price_id = models.ForeignKey(Carpet, on_delete=models.CASCADE, related_name='cartitems')
    count = models.PositiveSmallIntegerField()