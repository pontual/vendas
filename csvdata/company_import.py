import csv
from random import randint

from django.db import transaction

from companies.models import Company


@transaction.atomic
def read_companies(csvfile):
    """ Run python manage.py shell in directory with csv file
    
    from csvdata.company_import import read_companies

    read_companies(FILENAME)
    """
    
    with open(csvfile, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            Company.objects.create(code=row[0], business_name=row[1])
