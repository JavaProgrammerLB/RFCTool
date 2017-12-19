#! /usr/local/bin/python3
import requests
import sys

argvs = sys.argv
if len(argvs) < 2: 
    print("Usage: ./rfc_downloader.py [rfc number]")
else:
    rfc_num = argvs[1]
    res = requests.get("https://tools.ietf.org/pdf/rfc{}.pdf".format(rfc_num))
    file = open("rfc{}.pdf".format(rfc_num), "wb")
    file.write(res.content)
    print("write finished")
