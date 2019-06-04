#!/bin/env python3

from mpmath import mp
import random, time, requests

mp.dps = 10000 # 10000 digits of PI

s = ("%s" % mp.pi).replace('.', '')
ind = random.randint(random.randint(0,2000), 6000) # random index
hentais = [s[i:i+6] for i in range(ind, len(s), 6)]

for hentai in hentais:
    time.sleep(0.5)
    try:
        r = requests.head("https://nhentai.net/g/%s/" % hentai)
        if r.status_code is not 200:
            continue
        print("https://nhentai.net/g/%s/" % hentai)
    except requests.ConnectionError:
        print("Check your internet connection.")
        break
