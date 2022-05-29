from django.db.models import Avg, signals
from django.dispatch import receiver

from store_app.models import Comment


@receiver(signals.post_save, sender=Comment)
def post_save_comment(sender, instance, created, **kwargs):
    """Сигналы после добавления комментария"""
    product = instance.product
    product.avg_rating = product.comments.all().aggregate(Avg('rating'))['rating__avg']
    product.save()


@receiver(signals.post_delete, sender=Comment)
def post_delete_comment(sender, instance, created=False, **kwargs):
    """Сигнал после удаления комментария"""
    product = instance.product
    comments = product.comments.all()
    if comments.count() == 0:
        product.avg_rating = None
    else:
        product.avg_rating = product.comments.all().aggregate(Avg('rating'))['rating__avg']
    product.save()
