import string
import sys

wordsfile = file("newSCOWL.txt")
words = wordsfile.readlines()
words = [i.split('\n',1)[0] for i in words]

anagram = {}
for i in words:
    key = list(i)
    key.sort()
    key = ''.join(key)
    key = key.lower()
    if key not in anagram:
        anagram[key] = [i]
    else:
        anagram[key].append(i)

inp = raw_input("Enter a word.\n")
word = inp.lower()
for i in list(word):
     if i not in string.ascii_lowercase:
         print "Error: Your word contains non-letter characters."
         sys.exit()

tmp = list(word)
tmp.sort()
tmp = ''.join(tmp)

if tmp in anagram:
    result = anagram[tmp]
    if word in anagram[tmp]:
        result.remove(word)
else:
    result=[]

if result:
    print result
else:
    print word[0].upper() + word[1:len(word)] + " has no anagrams."
