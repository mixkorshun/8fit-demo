# Generated by Django 2.0.6 on 2018-06-27 23:16

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpageblock',
            name='content',
            field=wagtail.core.fields.RichTextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='landingpageblock',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='landings.LandingPage', verbose_name='page'),
        ),
    ]