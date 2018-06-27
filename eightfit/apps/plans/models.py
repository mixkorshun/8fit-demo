from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

from .fields import PriceField


class Plan(models.Model):
    CURRENCY_EUR = 'eur'
    CURRENCY_USD = 'usd'

    title = models.CharField(max_length=255, verbose_name=_('name'))
    stripe_plan = models.CharField(max_length=255, verbose_name=_('plan'))

    price = PriceField(verbose_name=_('price'))
    currency = models.CharField(max_length=8, choices=(
        (CURRENCY_EUR, 'EUR'),
        (CURRENCY_USD, 'USD'),
    ), default=CURRENCY_EUR, verbose_name=_('currency'))

    panels = [
        FieldPanel('title'),

        MultiFieldPanel(
            (
                FieldPanel('price'),
                FieldPanel('currency'),
            ),
            heading=_("Price"),
        ),

        MultiFieldPanel(
            (
                FieldPanel('stripe_plan'),
            ),
            heading=_("Stripe"),
        ),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('plan')
        verbose_name_plural = _('plans')


class Offer(ClusterableModel):
    title = models.CharField(max_length=255)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT,
                             related_name='offers')

    discount = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_('discount, %')
    )
    price = PriceField(
        null=True, blank=True,
        verbose_name=_('price'),
        help_text=_('Specify total price for offer. By default offer price '
                    'is: (plan price) - (discount). But you can manually '
                    'override it by specifying this field.')
    )

    expire_at = models.DateTimeField(null=True, blank=True,
                                     verbose_name=_('expire at'))

    panels = [
        FieldPanel('title'),
        FieldPanel('plan'),

        MultiFieldPanel(
            (
                FieldPanel('discount'),
                FieldPanel('price'),
            ),
            heading=_('Discount')
        ),

        MultiFieldPanel(
            (
                FieldPanel('expire_at'),
            ),
            heading=_('Options')
        )
    ]

    def get_price(self):
        if self.price is not None:
            return self.price

        k = (100 - self.discount) / 100
        price = k * float(self.plan.price)
        price = round(price, 2)
        return Decimal.from_float(price)

    get_price.short_description = _('total price')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('offer')
        verbose_name_plural = _('offers')
