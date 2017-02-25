import string
import sys
import itertools

wordsfile = file("newSCOWL.txt")
words = wordsfile.readlines()
words = [i.split('\n',1)[0] for i in words]

combos = {}
for i in words:
    key = list(i)
    key.sort()
    key = ''.join(key)
    key = key.lower()
    if key not in combos:
        combos[key] = [i]
    else:
        combos[key].append(i)

inp = raw_input("Enter a word.\n")
word = inp.lower()
for i in list(word):
     if i not in string.ascii_lowercase:
         print "Error: Your word contains non-letter characters."
         sys.exit()

tmp = list(word)
tmp.sort()
tmp = ''.join(tmp)

if tmp in combos:
    result = combos[tmp]
    if word in combos[tmp]:
        result.remove(word)
else:
    print "Error: " + word[0].upper() + word[1:len(word)] + " is not in the dictionary."
    sys.exit()

if len(result) == 0:
    print word[0].upper() + word[1:len(word)] + " has no anagrams."
else:
    print result
    result1 = []
    for x in range(len(word)):
        split = list(word)
        split.remove(split[x])
        split.sort()
        split = ''.join(split)
        if split in combos:
            result1 = result1 + combos[split]
    print result1
