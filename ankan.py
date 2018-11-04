import csv
import requests
import xml.etree.ElementTree as ET


l = []
tree = ET.parse('Zapata_rail.xml')
root=tree.getroot()
f = open("demofile.txt","w")
for name in root.iter('{http://www.mediawiki.org/xml/export-0.10/}username'):
    l.append(name.text)
    f.write(name.text)
    f.write("\n")
for name in root.iter('{http://www.mediawiki.org/xml/export-0.10/}ip'):
    l.append(name.text)
    f.write(name.text)
    f.write("\n")

#https://en.wikipedia.org/w/index.php?title=Special:Contributions&offset=20070214050528&limit=500&contribs=user&target=Stavenn&namespace=&tagfilter=&start=&end=