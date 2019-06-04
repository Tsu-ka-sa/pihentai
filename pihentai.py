#!/bin/env python3

from mpmath import mp
import random, time, requests, sys, re

mp.dps = 10000 # 10000 digits of PI

tags = False
if len(sys.argv) > 1:
    if sys.argv[1] == "-t":
       if len(sys.argv) < 3:
           print("This option requires at least one tag")
           exit(1)
       tags = sys.argv[2:len(sys.argv)]

s = ("%s" % mp.pi).replace('.', '')
ind = random.randint(random.randint(0,2000), 6000) # random index
hentais = [s[i:i+6] for i in range(ind, len(s), 6)]

for hentai in hentais:
    hentai = int(hentai)
    time.sleep(0.6)
    try:
        r = requests.get("https://nhentai.net/g/%s/" % hentai)
        if r.status_code is not 200:
            continue
        if tags is False:
            print("https://nhentai.net/g/%s/" % hentai)
        else:
            t = re.search(r'Tags:\n.*', r.text)
            t = re.sub(r'(>)([^\s]*)\s([^\s]*)(\s<)', r'\1\2_\3\4',t.group(0)[12:len(t.group(0))])
            t = re.sub(re.compile('<.*?>'), '', t)
            t = re.sub(re.compile('\(.*?\)'), '', t)
            issub = set(tags).issubset(set(t.split(" ")))
            if not issub:
                continue
            print("https://nhentai.net/g/%s/ ( %s)" % (hentai, t))
    except requests.ConnectionError:
        print("Check your internet connection.")
        break
