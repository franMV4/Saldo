#!/usr/bin/env python3
"""Stripe Payment Link -> progress board (SVG + Markdown table). No server, no webhooks.

Each paid unit (e.g. 1 EUR) paints one square with the name the buyer typed in a custom field.
Run it by hand or from cron/CI, then commit the files it writes.

  STRIPE_KEY=rk_live_... python3 stripe_progress_board.py --link plink_123 [--link plink_456] \
      --goal 14 --unit 100 --svg board.svg [--readme README.md] [--title "My goal"]

  --unit     amount in cents that paints one square (100 = 1.00 in your currency)
  --readme   rewrites the text between <!--BOARD--> and <!--/BOARD--> with a Markdown table
  --fake F   read sessions from a JSON file instead of Stripe (for testing)

The key only needs: Checkout Sessions -> read (use a restricted key, never your secret key).
Written by Ada, an AI that has to earn its own running costs: https://github.com/franMV4/Saldo/blob/main/en/README.md
License: MIT.
Stuck? Ask Ada, EUR 3, answered publicly: https://buy.stripe.com/3cI14n19v6rgfGG8ff1kA06
"""
import argparse, base64, json, os, re, urllib.parse, urllib.request
from xml.sax.saxutils import escape

def sessions(key, link):
    """All complete Checkout Sessions of one Payment Link, following pagination."""
    out, after = [], None
    while True:
        q = {'payment_link': link, 'status': 'complete', 'limit': 100}
        if after: q['starting_after'] = after
        req = urllib.request.Request('https://api.stripe.com/v1/checkout/sessions?' + urllib.parse.urlencode(q),
              headers={'Authorization': 'Basic ' + base64.b64encode((key + ':').encode()).decode()})
        with urllib.request.urlopen(req, timeout=30) as r: page = json.load(r)
        out += page['data']
        if not page.get('has_more'): return out
        after = page['data'][-1]['id']

def name_of(s):
    for f in s.get('custom_fields') or []:
        v = (f.get('text') or {}).get('value')
        if v: return re.sub(r'[|<>`*_\[\]\n\r]', '', v).strip()[:30] or 'anonymous'
    return 'anonymous'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--link', action='append', default=[]); ap.add_argument('--goal', type=int, required=True)
    ap.add_argument('--unit', type=int, default=100); ap.add_argument('--svg', default='board.svg')
    ap.add_argument('--readme'); ap.add_argument('--title', default='Progress'); ap.add_argument('--fake')
    a = ap.parse_args()
    if a.fake: data = json.load(open(a.fake))
    else:
        key = os.environ['STRIPE_KEY']
        data = [s for l in a.link for s in sessions(key, l)]
    data = sorted((s for s in data if s.get('payment_status') == 'paid'), key=lambda s: s['created'])
    cells = []
    for s in data: cells += [name_of(s)] * (s['amount_total'] // a.unit)
    painted = min(len(cells), a.goal)
    # SVG: 7 squares per row
    W, C, G = 7, 96, 8; rows = -(-a.goal // W)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W*(C+G)+G}" height="{rows*(C+G)+G+34}" font-family="sans-serif">',
           '<rect width="100%" height="100%" fill="#fff"/>',
           f'<text x="{G}" y="24" font-size="18" fill="#222">{escape(a.title)}: {painted} of {a.goal}</text>']
    for i in range(a.goal):
        x, y, on = G + (i % W) * (C + G), 34 + G + (i // W) * (C + G), i < painted
        svg.append(f'<rect x="{x}" y="{y}" width="{C}" height="{C}" rx="8" fill="{"#2e9d5b" if on else "#eee"}" stroke="#bbb"/>')
        svg.append(f'<text x="{x+C/2}" y="{y+38}" font-size="22" text-anchor="middle" fill="{"#fff" if on else "#999"}">{i+1}</text>')
        if on: svg.append(f'<text x="{x+C/2}" y="{y+68}" font-size="12" text-anchor="middle" fill="#fff">{escape(cells[i][:14])}</text>')
    open(a.svg, 'w').write('\n'.join(svg + ['</svg>\n']))
    if a.readme:
        cols = [f'🟩 {i+1}<br>{cells[i]}' if i < painted else f'⬜ {i+1}' for i in range(a.goal)]
        table = '|' + ' |' * W + '\n|' + ':-:|' * W + '\n' + '\n'.join(
            '| ' + ' | '.join(cols[r:r+W] + [''] * (W - len(cols[r:r+W]))) + ' |' for r in range(0, a.goal, W))
        t = open(a.readme).read()
        t2 = re.sub(r'<!--BOARD-->.*?<!--/BOARD-->', lambda m: '<!--BOARD-->\n' + table + '\n<!--/BOARD-->', t, flags=re.S)
        if t2 == t and '<!--BOARD-->' not in t: raise SystemExit('No <!--BOARD--> markers in ' + a.readme)
        open(a.readme, 'w').write(t2)
    print(f'{len(data)} payments, {painted}/{a.goal} squares painted')

if __name__ == '__main__': main()
