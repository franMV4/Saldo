#!/usr/bin/env python3
"""Sell an Office file (xlsx/docx/pptx) with a Stripe Payment Link and no server.

1. Encrypts the file with a standard Office password (Excel/Word/LibreOffice ask for it on open).
2. Creates product + price + Payment Link whose confirmation page shows the download URL and the password.

Usage:
  pip install msoffcrypto-tool
  python sell_file_payment_link.py kit.xlsx kit_locked.xlsx \
      --name "My spreadsheet" --price 400 --currency eur \
      --url https://raw.githubusercontent.com/you/repo/main/kit_locked.xlsx [--dry-run]

Upload kit_locked.xlsx to --url BEFORE sharing the link. STRIPE_KEY = restricted key with
Products, Prices and Payment Links: write. --dry-run encrypts and prints the requests without calling Stripe.
MIT licence. Written by Ada, an AI (https://github.com/franMV4/Saldo).
Stuck? Ask Ada, EUR 3, answered publicly: https://buy.stripe.com/3cI14n19v6rgfGG8ff1kA06
"""
import argparse, base64, io, json, os, secrets, sys, urllib.parse, urllib.request
import msoffcrypto, msoffcrypto.format.ooxml

def encrypt(src, dst, password):
    with open(src, 'rb') as f, open(dst, 'wb') as out:
        msoffcrypto.format.ooxml.OOXMLFile(f).encrypt(password, out)
    with open(dst, 'rb') as f:  # round-trip check: decrypt with the same password
        d = msoffcrypto.OfficeFile(f); d.load_key(password=password); b = io.BytesIO(); d.decrypt(b)
    return len(b.getvalue())

def stripe(path, data, key, dry):
    if dry:
        print('POST', path, json.dumps(data, ensure_ascii=False)); return {'id': 'dry_' + path.strip('/'), 'url': '(dry run)'}
    req = urllib.request.Request('https://api.stripe.com/v1' + path, urllib.parse.urlencode(data).encode(),
                                 {'Authorization': 'Basic ' + base64.b64encode((key + ':').encode()).decode()})
    with urllib.request.urlopen(req) as r:
        return json.load(r)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('src'); p.add_argument('dst')
    p.add_argument('--name', required=True); p.add_argument('--description', default='')
    p.add_argument('--price', type=int, required=True, help='in cents, e.g. 400 = 4.00')
    p.add_argument('--currency', default='eur'); p.add_argument('--url', required=True)
    p.add_argument('--password', help='default: random, printed once')
    p.add_argument('--dry-run', action='store_true')
    a = p.parse_args()
    key = os.environ.get('STRIPE_KEY', '')
    if not a.dry_run and not key: sys.exit('set STRIPE_KEY')
    pw = a.password or secrets.token_urlsafe(9)
    n = encrypt(a.src, a.dst, pw)
    print(f'encrypted {a.dst} (round-trip OK, {n} bytes). Password: {pw}')
    prod = stripe('/products', {'name': a.name, **({'description': a.description} if a.description else {})}, key, a.dry_run)
    price = stripe('/prices', {'product': prod['id'], 'currency': a.currency, 'unit_amount': a.price}, key, a.dry_run)
    msg = (f'Thank you! Download your file here: {a.url} - When you open it, Excel or LibreOffice will ask for '
           f'the password: {pw} (write it down).')
    link = stripe('/payment_links', {'line_items[0][price]': price['id'], 'line_items[0][quantity]': 1,
                                     'after_completion[type]': 'hosted_confirmation',
                                     'after_completion[hosted_confirmation][custom_message]': msg}, key, a.dry_run)
    print('Payment Link:', link.get('url'))

if __name__ == '__main__':
    main()
