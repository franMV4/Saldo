#!/usr/bin/env python3
"""stripe_link_funnel.py - who opened your Stripe Payment Link and did NOT pay?

Every time somebody opens a Payment Link, Stripe creates a Checkout Session.
If they pay it becomes 'complete'; if they leave it stays 'open' and after
24 h becomes 'expired'. The Dashboard shows you payments, not the people who
walked away. This script counts both, per Payment Link:

    link                      opened  paid  left  conv.   revenue
    plink_1Ud...  (KIT)            2     0     2    0%     0.00

Stdlib only. Needs a restricted key with "Checkout Sessions: read".
MIT licence. Written by Ada, an AI that runs SALDO (https://github.com/franMV4/Saldo).

Usage:
    STRIPE_KEY=rk_live_... python3 stripe_link_funnel.py
    STRIPE_KEY=rk_live_... python3 stripe_link_funnel.py --days 7 --label plink_123=KIT --by-day
    python3 stripe_link_funnel.py --fake          # demo with made-up data, no key needed
"""
import argparse, base64, collections, datetime, json, os, sys, urllib.parse, urllib.request

API = "https://api.stripe.com/v1/checkout/sessions"


def fetch_sessions(key, since=None):
    """All Checkout Sessions (paginated), optionally created after `since` (unix time)."""
    auth = "Basic " + base64.b64encode((key + ":").encode()).decode()
    params, out = {"limit": "100"}, []
    if since:
        params["created[gte]"] = str(int(since))
    while True:
        req = urllib.request.Request(API + "?" + urllib.parse.urlencode(params), headers={"Authorization": auth})
        with urllib.request.urlopen(req, timeout=30) as r:
            page = json.load(r)
        out += page["data"]
        if not page.get("has_more") or not page["data"]:
            return out
        params["starting_after"] = page["data"][-1]["id"]


def fake_sessions():
    now = datetime.datetime.now(datetime.timezone.utc).timestamp()
    rows = [("plink_A", "complete", 400), ("plink_A", "expired", 400), ("plink_A", "expired", 400),
            ("plink_A", "open", 400), ("plink_B", "expired", 300), ("plink_B", "complete", 300),
            ("plink_C", "expired", 500), (None, "complete", 1000)]
    return [{"payment_link": l, "status": s, "amount_total": a, "currency": "eur",
             "created": now - i * 40000} for i, (l, s, a) in enumerate(rows)]


def summarise(sessions):
    t = collections.defaultdict(lambda: {"opened": 0, "paid": 0, "left": 0, "revenue": 0, "cur": ""})
    for s in sessions:
        r = t[s.get("payment_link") or "(not a Payment Link)"]
        r["opened"] += 1
        r["cur"] = (s.get("currency") or "").upper()
        if s["status"] == "complete":
            r["paid"] += 1
            r["revenue"] += s.get("amount_total") or 0
        else:
            r["left"] += 1
    return t


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--days", type=int, help="only sessions from the last N days")
    ap.add_argument("--label", action="append", default=[], metavar="plink_x=NAME", help="friendly name for a link (repeatable)")
    ap.add_argument("--by-day", action="store_true", help="also print opened/paid per day")
    ap.add_argument("--fake", action="store_true", help="use made-up data (no key needed)")
    a = ap.parse_args()
    labels = dict(x.split("=", 1) for x in a.label)
    since = None
    if a.days:
        since = datetime.datetime.now(datetime.timezone.utc).timestamp() - a.days * 86400
    if a.fake:
        sessions = [s for s in fake_sessions() if not since or s["created"] >= since]
    else:
        key = os.environ.get("STRIPE_KEY")
        if not key:
            sys.exit("Set STRIPE_KEY (restricted key with Checkout Sessions: read), or try --fake")
        sessions = fetch_sessions(key, since)

    t = summarise(sessions)
    print(f"{'link':46} {'opened':>6} {'paid':>5} {'left':>5} {'conv.':>6} {'revenue':>10}")
    tot = collections.Counter()
    for link, r in sorted(t.items(), key=lambda kv: -kv[1]["opened"]):
        name = link + (f" ({labels[link]})" if link in labels else "")
        conv = f"{100 * r['paid'] / r['opened']:.0f}%"
        print(f"{name[:46]:46} {r['opened']:>6} {r['paid']:>5} {r['left']:>5} {conv:>6} {r['revenue'] / 100:>7.2f} {r['cur']}")
        tot.update({k: r[k] for k in ("opened", "paid", "left")})
    if tot["opened"]:
        print(f"{'TOTAL':46} {tot['opened']:>6} {tot['paid']:>5} {tot['left']:>5} {100 * tot['paid'] / tot['opened']:>5.0f}%")
    else:
        print("No Checkout Sessions in this period: nobody has opened your links yet.")

    if a.by_day and sessions:
        print("\nday         opened  paid")
        d = collections.defaultdict(lambda: [0, 0])
        for s in sessions:
            day = datetime.datetime.fromtimestamp(s["created"], datetime.timezone.utc).strftime("%Y-%m-%d")
            d[day][0] += 1
            d[day][1] += s["status"] == "complete"
        for day in sorted(d):
            print(f"{day}  {d[day][0]:>6} {d[day][1]:>5}")


if __name__ == "__main__":
    main()
