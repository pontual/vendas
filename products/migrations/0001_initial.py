# Generated by Django 2.1.1 on 2018-09-25 12:45

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32)),
                ('name', models.CharField(blank=True, max_length=120)),
                ('active', models.BooleanField(default=True)),
                ('ean', models.CharField(blank=True, max_length=32)),
                ('quantity_per_box', models.IntegerField(default=0)),
                ('ncm', models.CharField(blank=True, max_length=32, verbose_name='NCM')),
                ('ii', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=6, verbose_name='I.I.')),
                ('cest', models.CharField(blank=True, max_length=20, verbose_name='CEST')),
                ('icms', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=6, verbose_name='ICMS')),
                ('ipi', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=6, verbose_name='IPI')),
                ('weight', models.IntegerField(default=0)),
                ('default_sale_price', models.DecimalField(decimal_places=4, default=Decimal('0.0'), max_digits=12)),
                ('default_sale_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transactions.Currency')),
            ],
            options={
                'ordering': ['code'],
            },
        ),
    ]
