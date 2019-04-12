#!/usr/bin/env python3.5
import sys
import lxml.html
import urllib.request
if(len(sys.argv) < 2):
    print("Dude")
    quit()
url = sys.argv[1]
request = urllib.request.urlopen(url)
t = lxml.html.parse(request)
print(t.find(".//title").text)
