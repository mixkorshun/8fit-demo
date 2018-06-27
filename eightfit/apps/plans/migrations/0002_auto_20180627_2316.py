# Generated by Django 2.0.6 on 2018-06-27 23:16

from django.db import migrations, models
import eightfit.apps.plans.fields


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='discount',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='discount, %'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='expire_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expire at'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=eightfit.apps.plans.fields.PriceField(blank=True, help_text='Specify total price for offer. By default offer price is: (plan price) - (discount). But you can manually override it by specifying this field.', max_digits=8, null=True, verbose_name='price'),
        ),
    ]
