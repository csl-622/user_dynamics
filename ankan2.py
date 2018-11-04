import csv
import requests
import xml.etree.ElementTree as ET
import html5lib
import bs4
import urllib


def loadRSS():
    # url of rss feed
    l=[]
    f = open("demofile.txt", "r")
    for x in f:
        #print(x)
        l.append(x.rstrip("\n"))
    print(l)
    #for k in l:
    url="https://en.wikipedia.org/w/index.php?limit=50&title=Special%3AContributions&contribs=user&target=Manxruler&namespace=&tagfilter=&start=&end="
    print(url)
    # creating HTTP response object from given url
    resp = requests.get(url)
    str="Manxruler.html"
    # saving the xml file
    with open(str, 'wb') as f:
        f.write(resp.content)


def main():
    # load rss from web to update existing xml file
    loadRSS()



if __name__ == "__main__":
    # calling main function
    main()
    f1 = open("Manxruler.html", "r")
    a=f1.read()
    soup=bs4.BeautifulSoup(a)
    tags=soup('a')
    for tag in tags:
        if tag.get('class',None)=="['mw-contributions-title']":
            print(tag.string)