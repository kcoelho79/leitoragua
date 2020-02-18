from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.error
import json

try:
    # html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
    html = urlopen("https://datastudio.google.com/reporting/188wX_8wKVwiG8VBhAGheljpcqU18Dov1/page/bCkF")
except urllib.error.HTTPError as e:
    print(e)
    print(e.code)
else:
    bsObj = BeautifulSoup(html, features="html.parser");
    equipamento = bsObj.find_all("div", {"class_":"cell word-wrap"})



    print(bsObj.prettify())
    #print(bsObj)
    print(equipamento)


