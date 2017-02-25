# NB \x7f


import string
import sys

wordsfile = file("OEDmeaning.txt")
raw = wordsfile.readlines()
raw = [i.split('\n',1)[0] for i in raw]

x=range(len(raw))
x.reverse()

words=[]

for i in raw:
    if "  " not in i:
        continue
    words.append(i)

oed = {'test':'entry'}

for j in words:
    for i in range(len(j)):
        if j[i] == " " and j[i+1] == " ":
            oed[j[0:i]] = j[i+2:len(j)]
            
for i in oed:
    

