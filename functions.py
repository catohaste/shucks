import string
import sys

def is_dict(word):
    word=word.upper()
    if word in words:
        return True
    else:
        return False

def valid_char(word):
    word=word.lower()
    for i in list(word):
        if i in string.ascii_lowercase:
            return True
        else:
            return False

def anagram(word, words):
    anag = {}
    
    for i in words:
        key = list(i)
        key.sort()
        key = ''.join(key)
        key = key.lower()
        if key not in anag:
            anag[key] = [i]
        else:
            anag[key].append(i)
    
    tmp = list(word)
    tmp.sort()
    tmp = ''.join(tmp)
    
    if tmp in anag:
        result = anag[tmp]
        if word in anag[tmp]:
            result.remove(word)
    else:
        result=[]

    return result
    
wordsfile = file("newSCOWL.txt")
words = wordsfile.readlines()
words = [i.split('\n',1)[0] for i in words]

inp = raw_input("Enter a word.\n")
word = inp.lower()

result = anagram(word, words)
if result:
    print result
else:
    print word + " has no anagrams."