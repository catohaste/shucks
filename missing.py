import string
import sys

inp = raw_input("Enter a word, with hyphens representing missing letters.\n")
word = inp.lower()
for i in list(word):
     if i not in string.ascii_lowercase and not "-":
         print "Error: Your word contains unexpected characters."
         sys.exit()

hyphens = []
for i in range(len(word)):
    if word[i] == '-':
        hyphens.append(i)

wordsfile = file("newSCOWL.txt")
words = wordsfile.readlines()
words = [i.split('\n',1)[0] for i in words]

missing = {}
for i in words:
    if len(i) == len(word):
        key = list(i)
        for j in hyphens:
            key[j] = '-'
        key = ''.join(key)
        #key = key.lower()
        if key in missing:
            missing[key].append(i)
        else:    
            missing[key] = [i]

if word in missing:
    print missing[word]
else:
    print "No words found for " + word
