from wagtail.contrib.modeladmin.options import modeladmin_register

from eightfit.apps.plans.admin import PlansAdminGroup

modeladmin_register(PlansAdminGroup)
