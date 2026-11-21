#!/usr/bin/env python3
"""Paid orders of a Stripe Payment Link -> CSV, with the custom field answers.
Usage: STRIPE_KEY=rk_... python3 stripe_link_orders_csv.py plink_XXX [--days 31] > orders.csv
Needs only 'Checkout Sessions: read'. Standard library only. By Ada (SALDO), MIT."""
import csv, json, os, sys, time, urllib.parse, urllib.request

def sessions(key, link, since):
    params = {"payment_link": link, "limit": 100, "created[gte]": since, "status": "complete"}
    while True:
        url = "https://api.stripe.com/v1/checkout/sessions?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"Authorization": "Bearer " + key})
        page = json.load(urllib.request.urlopen(req))
        yield from page["data"]
        if not page["has_more"]:
            return
        params["starting_after"] = page["data"][-1]["id"]

def field_value(f):
    for kind in ("text", "numeric", "dropdown"):
        if f.get(kind):
            return f[kind].get("value") or ""
    return ""

def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        sys.exit(__doc__)
    days = int(args[args.index("--days") + 1]) if "--days" in args else 31
    since = int(time.time()) - days * 86400
    rows = []
    for s in sessions(os.environ["STRIPE_KEY"], args[0], since):
        d = s.get("customer_details") or {}
        row = {"date": time.strftime("%Y-%m-%d %H:%M", time.gmtime(s["created"])),
               "email": d.get("email") or "", "name": d.get("name") or "",
               "amount": (s.get("amount_total") or 0) / 100, "currency": (s.get("currency") or "").upper()}
        for f in s.get("custom_fields") or []:
            row[f["key"]] = field_value(f)
        rows.append(row)
    cols = []
    for r in rows:
        cols += [k for k in r if k not in cols]
    w = csv.DictWriter(sys.stdout, fieldnames=cols or ["date", "email", "name", "amount", "currency"])
    w.writeheader()
    w.writerows(rows)
    print(f"{len(rows)} paid orders in the last {days} days", file=sys.stderr)

if __name__ == "__main__":
    main()
