#! /usr/local/bin/python3
import requests
import sys
from bs4 import BeautifulSoup

argvs = sys.argv
usage_string = "[ERROR] Usage: python rfc_downloader.py [rfc number]"
if len(argvs) < 2: 
    print(usage_string)
else:
    rfc_num = argvs[1]
    if not rfc_num.isdigit():
        print(usage_string, "rfc number={}, is not a digit".format(rfc_num))
    else:
        res = requests.get("https://tools.ietf.org/pdf/rfc{}".format(rfc_num))
        # get doc name
        res_html = requests.get("https://tools.ietf.org/html/rfc{}".format(rfc_num))
        soup = BeautifulSoup(res_html.text, "lxml")
        doc_name = soup.title.string
        # write file
        file_name = "{}.pdf".format(doc_name)
        file_name = file_name.replace("/", "-")
        file = open(file_name, "wb")
        file.write(res.content)
        print("Downloaded {}".format(file_name))
