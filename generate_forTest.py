#!/usr/bin/env python3
import csv
import hashlib
import os
import random

DIR = os.path.abspath(os.path.dirname(__file__))
FILES = {
    'test_clothing.csv': ('Blouses', 'Shirts', 'Tanks', 'Cardigans', 'Pants', 'Capris', '"Gingham" Shorts',),
    'test_accessories.csv': ('Watches', 'Wallets', 'Purses', 'Satchels',)
}


def write_file(writer, length, categories):
    writer.writerow(['email_hash', 'category'])
    for i in range(0, length):
        writer.writerow([
            hashlib.sha256('tech+test{}@pmg.com'.format(i).encode('utf-8')).hexdigest(),
            random.choice(categories),
        ])


def main():
    for fn, categories in FILES.items():
        with open(os.path.join(DIR, 'test_csv', fn), 'w', encoding='utf-8') as fh:
            write_file(
                csv.writer(fh, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL),
                20,
                categories
            )

if __name__ == '__main__':
    main()
