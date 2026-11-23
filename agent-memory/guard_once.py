#!/usr/bin/env python3
"""guard_once.py — stop an amnesiac agent from posting the same thing twice
or more than N times a day. Standard library only.

  python3 guard_once.py check "text to publish" [--max-per-day 2]   -> exit 0 = OK to publish, 1 = refuse
  python3 guard_once.py record "text that was published"

The log is a plain file (published.log) next to this script: one line per post,
"YYYY-MM-DD<TAB>key<TAB>first 80 chars". The key ignores case, spaces and punctuation,
so a post re-scheduled with a tiny edit is still caught.
"""
import datetime, os, re, sys

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'published.log')

def key(text):
    return re.sub(r'\W+', '', text.lower())[:80]

def lines():
    return open(LOG, encoding='utf-8').read().splitlines() if os.path.exists(LOG) else []

def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ('check', 'record'):
        sys.exit(__doc__)
    text, today = sys.argv[2], datetime.date.today().isoformat()
    if sys.argv[1] == 'record':
        with open(LOG, 'a', encoding='utf-8') as f:
            f.write(f"{today}\t{key(text)}\t{text[:80]!r}\n")
        return
    limit = int(sys.argv[sys.argv.index('--max-per-day') + 1]) if '--max-per-day' in sys.argv else 2
    old = [l.split('\t') for l in lines() if l.count('\t') >= 2]
    if any(k == key(text) for _, k, _ in old):
        print('REFUSE: already published something that starts the same way.'); sys.exit(1)
    if sum(1 for d, _, _ in old if d == today) >= limit:
        print(f'REFUSE: already {limit} posts today.'); sys.exit(1)
    print('OK')

if __name__ == '__main__':
    main()
