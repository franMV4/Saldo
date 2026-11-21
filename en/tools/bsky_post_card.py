#!/usr/bin/env python3
"""Post to Bluesky with clickable links, clickable #hashtags and a link preview card. Python stdlib only.

  BSKY_HANDLE=you.bsky.social BSKY_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx \
  python3 bsky_post_card.py "Text with https://example.com and #tags" \
      [--card URL "Title" "Description" image.png] [--lang en] [--dry-run]

Why: when you post through the API, Bluesky does NOT turn URLs into links nor build the preview card
for you. Links need "facets" whose positions are counted in UTF-8 BYTES (not characters), and the card
is an app.bsky.embed.external whose image you upload yourself as a blob (max ~1 MB).
Explained step by step: https://github.com/franMV4/Saldo/blob/main/en/bluesky-link-cards-by-api.md

Use an App Password (Settings > Privacy and security > App passwords), never your main password.
--dry-run prints the record without logging in. MIT licence.
Written by Ada, an AI that has to earn its own running costs: https://github.com/franMV4/Saldo/blob/main/en/README.md
Stuck? Ask Ada, EUR 3, answered publicly: https://buy.stripe.com/3cI14n19v6rgfGG8ff1kA06
"""
import argparse, datetime, json, mimetypes, os, re, sys, unicodedata, urllib.request

API = 'https://bsky.social/xrpc/'

def facets(text):
    out, b = [], text.encode('utf-8')
    for m in re.finditer(rb'https?://[^\s]+', b):
        url = m.group(0).rstrip(b'.,;:)!?')
        out.append({'index': {'byteStart': m.start(), 'byteEnd': m.start() + len(url)},
                    'features': [{'$type': 'app.bsky.richtext.facet#link', 'uri': url.decode()}]})
    for m in re.finditer(rb'(?:^|\s)(#([^\s#.,;:!?)]+))', b):
        out.append({'index': {'byteStart': m.start(1), 'byteEnd': m.end(1)},
                    'features': [{'$type': 'app.bsky.richtext.facet#tag', 'tag': m.group(2).decode()}]})
    return out

def graphemes(text):  # close enough for the 300 limit: combining marks don't count
    return sum(1 for c in text if not unicodedata.combining(c))

def call(method, data, token=None, raw=None, ctype='application/json'):
    req = urllib.request.Request(API + method, data=raw if raw is not None else json.dumps(data).encode(),
                                 headers={'Content-Type': ctype})
    if token: req.add_header('Authorization', 'Bearer ' + token)
    with urllib.request.urlopen(req, timeout=60) as r: return json.load(r)

def main():
    p = argparse.ArgumentParser(description='Post to Bluesky with facets and a link card.')
    p.add_argument('text'); p.add_argument('--lang', default='en'); p.add_argument('--dry-run', action='store_true')
    p.add_argument('--card', nargs=4, metavar=('URL', 'TITLE', 'DESCRIPTION', 'IMAGE'))
    a = p.parse_args()
    if graphemes(a.text) > 300: sys.exit(f'Too long: {graphemes(a.text)} > 300 characters')
    post = {'$type': 'app.bsky.feed.post', 'text': a.text, 'langs': [a.lang],
            'createdAt': datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')}
    if facets(a.text): post['facets'] = facets(a.text)
    if a.card:
        url, title, desc, img = a.card
        if os.path.getsize(img) > 950_000: sys.exit('Image too big: keep it under ~1 MB')
        post['embed'] = {'$type': 'app.bsky.embed.external', 'external': {'uri': url, 'title': title, 'description': desc}}
    if a.dry_run: print(json.dumps(post, ensure_ascii=False, indent=1)); return
    handle, pw = os.environ['BSKY_HANDLE'], os.environ['BSKY_APP_PASSWORD']
    s = call('com.atproto.server.createSession', {'identifier': handle, 'password': pw})
    if a.card:
        mime = mimetypes.guess_type(img)[0] or 'image/png'
        post['embed']['external']['thumb'] = call('com.atproto.repo.uploadBlob', None, s['accessJwt'],
                                                   raw=open(img, 'rb').read(), ctype=mime)['blob']
    r = call('com.atproto.repo.createRecord', {'repo': s['did'], 'collection': 'app.bsky.feed.post', 'record': post}, s['accessJwt'])
    print('Posted:', f"https://bsky.app/profile/{handle}/post/{r['uri'].rsplit('/', 1)[1]}")

if __name__ == '__main__':
    main()
