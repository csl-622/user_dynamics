import os
import sys
import collections
import xml.etree.ElementTree as etr
import re
'''
to run this file - python sid.py filename, eg - python sid.py wiki.xml
This function creates a dictionary 'a' which has key as username and the value as list of titles revised by the user.
The list contain only those usernames whose revision are above threshold bytes.
'''

def users_list(threshlold,root):
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
                        a[u.text].append(n.text)
    return a

st=sys.argv[1]+".xml"
tree = etr.parse(st)
root= tree.getroot()
users = users_list(0,root)
username = list(users.keys())
text = list(users.values())
if not os.path.isdir(sys.argv[1]):
   os.makedirs(sys.argv[1])
#a = os.path.join("India")
count = 0
for i in range(len(username)):
    count += 1
    #print(count)
    a = open(os.path.join(sys.argv[1],str(username[i]).replace(':','-').replace('?','-').replace('|','-').replace('/','-').replace("\\","-")+'.txt'),'w',encoding = 'utf-8')
    #if len(text[i]) > 1:
     #   print(username[i])
    for j in range(0,len(text[i])):
        #text[i][j].replace('[',' ').replace(']',' ').replace('<')
        new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', text[i][j])
        text[i][j] = new_str
        a.write(new_str)
        a.write('\n-------------------||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||---------------------------\n')
    a.close()
print ("The edits are written in the respective text files in the folder of the same name as the xml file.")    
#print(users[2])
