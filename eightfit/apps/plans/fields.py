from django.db import models


class PriceField(models.DecimalField):

    def __init__(self, **kwargs):
        assert 'decimal_places' not in kwargs

        kwargs.setdefault('max_digits', 8)
        kwargs['decimal_places'] = 2
        super().__init__(**kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()

        del kwargs['decimal_places']

        return name, path, args, kwargs
