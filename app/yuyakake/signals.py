from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, CakeReview, Cake, CakeSample


@receiver(post_save, sender=Order)
def create_cake_review(sender, instance, created, **kwargs):
    if created:
        cake = instance.cake
        user = instance.user
        rating = instance.cake_rating
        review = instance.cake_review
        CakeReview.objects.create(cake=cake, user=user, rating=rating, review=review)


@receiver(post_save, sender=Cake)
def create_cake_review(sender, instance, created, **kwargs):
    if created:
        cake = instance
        name = instance.name
        description = instance.description
        image = instance.image
        base = instance.base
        layers = instance.layers
        filling = instance.filling
        meringue = instance.meringue
        size = instance.size
        CakeSample.objects.create(
            cake=cake,
            name=name,
            description=description,
            image=image,
            base=base,
            layers=layers,
            filling=filling,
            meringue=meringue,
            size=size,
        )

