from django.contrib.auth.models import User
from django.db import models


class CakeBase(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='base/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image.url if self.image else ''
        }

class CakeLayer(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='layers/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image.url if self.image else ''
        }

class CakeMeringue(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='meringues/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image.url if self.image else ''
        }

class CakeSize(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='sizes/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image.url if self.image else ''
        }

class Cake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='cakes/')
    base = models.ForeignKey(CakeBase, on_delete=models.CASCADE)
    layers = models.ForeignKey(CakeLayer, on_delete=models.CASCADE)
    filling = models.TextField()
    meringue = models.ForeignKey(CakeMeringue, on_delete=models.CASCADE)
    size = models.ForeignKey(CakeSize, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str__(self):
        return self.name


from django.db.models.signals import post_save
from django.dispatch import receiver

class CakeSample(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.PROTECT, related_name='samples')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='samples/')
    base = models.ForeignKey(CakeBase, on_delete=models.PROTECT)
    layers = models.ForeignKey(CakeLayer, on_delete=models.PROTECT)
    filling = models.TextField()
    meringue = models.ForeignKey(CakeMeringue, on_delete=models.PROTECT)
    size = models.ForeignKey(CakeSize, on_delete=models.PROTECT)
    #datecreated

    def __str__(self):
        return f"{self.name} ({self.cake.name})"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image.url if self.image else '',
            'base': self.base.name if self.image else '',
            'layers': self.layers.name if self.image else '',
            'filling': self.filling if self.image else '',
            'meringue': self.meringue.name if self.image else '',
            'size': self.size.name if self.image else '',
        }
    
class CakeReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cake.name} review by {self.user.username}"
class Order(models.Model):
    STATE_CHOICES = [
        ('P', 'Pendiente'),
        ('E', 'En preparación'),
        ('L', 'Listo para recoger'),
        ('C', 'Completado'),
        ('X', 'Cancelado'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=200)
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    notes = models.TextField(blank=True)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.username} ({self.delivery_date})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    sample = models.ForeignKey(CakeSample, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.cake.name} ({self.sample.name})"
