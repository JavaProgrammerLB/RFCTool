#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import requests

index_url = "https://tools.ietf.org/rfc/index"
res = requests.get(index_url)
html_doc = res.text

soup = BeautifulSoup(html_doc, "lxml")
rs  = soup.find_all("pre")
rs_0 = rs[0]
index_doc = rs_0.get_text()

index_file = open("index.txt", "w")
index_file.write(index_doc)

print("Done")

