import os
import csv
from decimal import Decimal

from django.db import transaction
from django.core.files import File

from products.models import Product
from transactions.models import Currency


@transaction.atomic
def read_products(csvfile, fotos_dir, currency_code):
    """ Run python manage.py shell in directory with csv file

    from csvdata.product_import import read_products

    read_products(FILENAME, FOTOS_DIR, "BRL")
    """
    curr = Currency.objects.get(code=currency_code)

    with open(csvfile, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            try:
                Product.objects.create(code=row[0],
                                       name=row[1],
                                       photo=File(open(os.path.join(fotos_dir, row[0]) + ".jpg", "rb")),
                                       default_sale_currency=curr,
                                       default_sale_price=Decimal(row[2].replace(',', '.')))
            except FileNotFoundError:
                print("No photo found for", row[0], "(skipped)")
