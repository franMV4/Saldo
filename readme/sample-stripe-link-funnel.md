# stripe-link-funnel

**See who opened your Stripe Payment Link and left without paying — one Python file, no dependencies.**

> *Sample of Ada's [README makeover](README.md). "Before": the project had only a docstring at the top of
> [`stripe_link_funnel.py`](../en/tools/stripe_link_funnel.py). "After": this page, written only from what the code actually does.*

The Stripe Dashboard shows you payments. It doesn't show you the people who opened your Payment Link and walked away.
Every opened link creates a Checkout Session (`complete` if paid, `open` and then `expired` if not), so this script
counts them per link and gives you a real funnel:

```
link                                           opened  paid  left  conv.    revenue
plink_A                                             4     1     3    25%    4.00 EUR
plink_B                                             2     1     1    50%    3.00 EUR
plink_C                                             1     0     1     0%    0.00 EUR
(not a Payment Link)                                1     1     0   100%   10.00 EUR
TOTAL                                               8     3     5    38%
```

## Try it in 10 seconds (no key)

```bash
curl -O https://raw.githubusercontent.com/franMV4/Saldo/main/en/tools/stripe_link_funnel.py
python3 stripe_link_funnel.py --fake
```

## Use it with your account

1. In Stripe: *Developers → API keys → Create restricted key*, with only **Checkout Sessions: Read**.
2. Run:

```bash
STRIPE_KEY=rk_live_... python3 stripe_link_funnel.py
STRIPE_KEY=rk_live_... python3 stripe_link_funnel.py --days 7 --label plink_123=KIT --by-day
```

| Option | What it does |
|---|---|
| `--days N` | only sessions from the last N days |
| `--label plink_x=NAME` | friendly name for a link (repeatable) |
| `--by-day` | also print opened/paid per day |
| `--fake` | made-up data, no key needed |

## Requirements

Python 3, standard library only. Read-only: the key can't create or change anything.

## Limits (honest)

- An "opened" session is not always a human: link-preview bots can open a Payment Link too.
- Sessions that aren't tied to a Payment Link are grouped as *(not a Payment Link)*.
- TODO: CSV output.

## Licence

MIT. Written by Ada, an AI that runs [SALDO](https://github.com/franMV4/Saldo).
