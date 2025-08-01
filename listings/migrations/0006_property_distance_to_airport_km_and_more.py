# Generated by Django 5.2.3 on 2025-07-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_property_owner_alter_propertyimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='distance_to_airport_km',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='distance_to_center_m',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='has_guaranteed_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='has_management_company',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='is_furnished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='ownership_type',
            field=models.CharField(choices=[('freehold', 'Freehold'), ('leasehold', 'Leasehold')], default='freehold', max_length=50),
        ),
        migrations.AddField(
            model_name='property',
            name='roi_percent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='yutree_score',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
