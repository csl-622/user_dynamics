import sys
import collections
import xml.etree.ElementTree as etr

'''

This function creates a dictionary 'a' which has key as username and the value as list of titles revised by the user.
The list contain only those usernames whose revision are above threshold bytes.

'''
def users_list(threshlold):
	a = collections.defaultdict(list)
	t=int(threshlold)
	for c in root:
		for n in c.iter():
			if n.tag=='title':
				title=n.text
			if n.tag=='username':
				u=n
			if n.tag=='ip':
				u=n				
			if n.tag=='text':
				 b=int(n.get('bytes'))
				 if b>t:
				 	if title not in a[u.text]:
						a[u.text].append(title)
		
	return a


tree = etr.parse(sys.argv[1])
root= tree.getroot()
print users_list(900)

