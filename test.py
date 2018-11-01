import sys
import collections
import xml.etree.ElementTree as etr

tree = etr.parse(sys.argv[1])
root= tree.getroot()
'''for name in root.iter('username'):
	l.append((name))

un=list(set(d.text for d in l))'''

'''gives a dictionary key as name of the user and value as the list of titles edited by the user '''
a = collections.defaultdict(list)
for c in root:
	for n in c.iter():
		if n.tag=='title':
			title=n.text
		if n.tag=='username':
			if title not in a[n.text]:
				a[n.text].append(title)

print "Total number of users : " + str(len(a.keys()))

print a


