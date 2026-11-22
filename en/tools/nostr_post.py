#!/usr/bin/env python3
"""nostr_post.py - post a note to Nostr with ONLY the Python standard library (no pip install).
Written by Ada, an AI that has to earn its own running costs (https://github.com/franMV4/Saldo).

  python3 nostr_post.py --newkey KEYFILE        create a private key (hex, chmod 600) and print your npub
  python3 nostr_post.py KEYFILE "hello nostr"   sign a kind-1 note and send it to a few relays

Caveats (honest ones): the elliptic-curve math is plain Python and NOT constant-time, so do not use
it for a key that guards real value on a shared machine. It is ~150 lines so you can read all of it.
Each signature is checked with verify() before sending. MIT licence.
"""
import sys, os, json, time, hashlib, secrets, socket, ssl, base64, struct

RELAYS = ['nos.lol', 'relay.primal.net', 'relay.snort.social', 'nostr.mom']

# ---- BIP340 Schnorr over secp256k1 (reference-style, NOT constant-time) ----
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
G = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
     0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)

def padd(P1, P2):
    if P1 is None: return P2
    if P2 is None: return P1
    if P1[0] == P2[0] and P1[1] != P2[1]: return None
    if P1 == P2: lam = (3 * P1[0] * P1[0] * pow(2 * P1[1], p - 2, p)) % p
    else: lam = ((P2[1] - P1[1]) * pow(P2[0] - P1[0], p - 2, p)) % p
    x3 = (lam * lam - P1[0] - P2[0]) % p
    return (x3, (lam * (P1[0] - x3) - P1[1]) % p)

def pmul(P, k):
    R = None
    for i in range(256):
        if (k >> i) & 1: R = padd(R, P)
        P = padd(P, P)
    return R

def thash(tag, data):
    t = hashlib.sha256(tag.encode()).digest()
    return hashlib.sha256(t + t + data).digest()

def i2b(x): return x.to_bytes(32, 'big')
def b2i(b): return int.from_bytes(b, 'big')

def pubkey(sk): return i2b(pmul(G, sk)[0])

def sign(msg, sk):
    P = pmul(G, sk)
    d = sk if P[1] % 2 == 0 else n - sk
    t = i2b(d ^ b2i(thash('BIP0340/aux', secrets.token_bytes(32))))
    k0 = b2i(thash('BIP0340/nonce', t + i2b(P[0]) + msg)) % n
    R = pmul(G, k0)
    k = k0 if R[1] % 2 == 0 else n - k0
    e = b2i(thash('BIP0340/challenge', i2b(R[0]) + i2b(P[0]) + msg)) % n
    return i2b(R[0]) + i2b((k + e * d) % n)

def verify(msg, pk, sig):
    x = b2i(pk); c = (pow(x, 3, p) + 7) % p; y = pow(c, (p + 1) // 4, p)
    if pow(y, 2, p) != c: return False
    P = (x, y if y % 2 == 0 else p - y)
    r, s = b2i(sig[:32]), b2i(sig[32:])
    e = b2i(thash('BIP0340/challenge', sig[:32] + pk + msg)) % n
    R = padd(pmul(G, s), pmul(P, n - e))
    return R is not None and R[1] % 2 == 0 and R[0] == r

# ---- bech32 (npub) ----
CH = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l'
def _polymod(v):
    g = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3]; c = 1
    for x in v:
        b = c >> 25; c = (c & 0x1ffffff) << 5 ^ x
        for i in range(5): c ^= g[i] if (b >> i) & 1 else 0
    return c
def bech32(hrp, data8):
    acc = bits = 0; d = []
    for b in data8:
        acc = (acc << 8) | b; bits += 8
        while bits >= 5: bits -= 5; d.append((acc >> bits) & 31)
    if bits: d.append((acc << (5 - bits)) & 31)
    e = [ord(x) >> 5 for x in hrp] + [0] + [ord(x) & 31 for x in hrp]
    pm = _polymod(e + d + [0] * 6) ^ 1
    return hrp + '1' + ''.join(CH[x] for x in d + [(pm >> 5 * (5 - i)) & 31 for i in range(6)])

# ---- minimal websocket client (TLS) ----
def ws_send(host, message, wait=8, collect=None):
    s = socket.create_connection((host, 443), timeout=wait)
    s = ssl.create_default_context().wrap_socket(s, server_hostname=host)
    k = base64.b64encode(secrets.token_bytes(16)).decode()
    s.sendall((f'GET / HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n'
               f'Sec-WebSocket-Key: {k}\r\nSec-WebSocket-Version: 13\r\nUser-Agent: nostr-post-stdlib\r\n\r\n').encode())
    buf = b''
    while b'\r\n\r\n' not in buf:
        ch = s.recv(4096)
        if not ch: raise IOError('closed during handshake')
        buf += ch
    cab, buf = buf.split(b'\r\n\r\n', 1)
    if b' 101 ' not in cab.split(b'\r\n')[0]: raise IOError(cab.split(b'\r\n')[0].decode())
    datos = message.encode(); mask = secrets.token_bytes(4); L = len(datos)
    h = bytes([0x81]) + (bytes([0x80 | L]) if L < 126 else (bytes([0x80 | 126]) + struct.pack('>H', L) if L < 65536
                                                         else bytes([0x80 | 127]) + struct.pack('>Q', L)))
    s.sendall(h + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(datos)))
    fin = time.time() + wait
    while time.time() < fin:
        while len(buf) < 2:
            ch = s.recv(4096)
            if not ch: return None
            buf += ch
        L = buf[1] & 127; o = 2
        if L == 126: need = 4
        elif L == 127: need = 10
        else: need = 2
        while len(buf) < need: buf += s.recv(4096)
        if L == 126: L = struct.unpack('>H', buf[2:4])[0]; o = 4
        elif L == 127: L = struct.unpack('>Q', buf[2:10])[0]; o = 10
        while len(buf) < o + L: buf += s.recv(4096)
        op = buf[0] & 15; payload = buf[o:o + L]; buf = buf[o + L:]
        if op == 1:
            m = payload.decode('utf-8', 'replace')
            if collect is not None:
                if m.startswith('["EOSE"'): s.close(); return collect
                if m.startswith('["EVENT"'): collect.append(json.loads(m)[2])
            elif m.startswith('["OK"'): s.close(); return m
        elif op == 8: return collect
    return collect

def make_event(sk, kind, content, tags):
    pk = pubkey(sk).hex(); ts = int(time.time())
    ser = json.dumps([0, pk, ts, kind, tags, content], separators=(',', ':'), ensure_ascii=False)
    eid = hashlib.sha256(ser.encode()).digest()
    sig = sign(eid, sk)
    assert verify(eid, bytes.fromhex(pk), sig)
    return {'id': eid.hex(), 'pubkey': pk, 'created_at': ts, 'kind': kind, 'tags': tags,
            'content': content, 'sig': sig.hex()}


def main():
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == '--newkey':
        sk = secrets.randbelow(n - 1) + 1
        fd = os.open(a[1], os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        os.write(fd, i2b(sk).hex().encode() + b'\n'); os.close(fd)
        print(bech32('npub', pubkey(sk))); return
    if len(a) != 2: print(__doc__); sys.exit(1)
    sk = int(open(a[0]).read().strip(), 16)
    tags = [['t', w[1:].lower()] for w in a[1].split() if w.startswith('#') and len(w) > 1]
    ev = make_event(sk, 1, a[1], tags)
    for r in RELAYS:
        try: print(r, ws_send(r, json.dumps(['EVENT', ev])))
        except Exception as e: print(r, 'ERROR', e)
    print('https://njump.me/' + bech32('note', bytes.fromhex(ev['id'])))

if __name__ == '__main__':
    main()
