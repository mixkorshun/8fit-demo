from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.modeladmin.options import (ModelAdmin, ModelAdminGroup)

from .models import Plan, Offer


class PlanModelAdmin(ModelAdmin):
    model = Plan
    menu_label = _('Plans')
    menu_icon = 'doc-full-inverse'
    list_display = ('title', 'price', 'currency')
    list_filter = ('currency',)
    search_fields = ('title',)


class OfferModelAdmin(ModelAdmin):
    model = Offer
    menu_label = _('Offers')
    menu_icon = 'doc-full-inverse'
    list_display = ('title', 'plan', 'discount', 'get_price')
    list_filter = ('plan', 'plan__currency')
    search_fields = ('title',)


class PlansAdminGroup(ModelAdminGroup):
    menu_label = _('Plans')
    menu_icon = 'folder-inverse'
    items = (
        PlanModelAdmin,
        OfferModelAdmin
    )
