
import string
import sys
import time

def is_doublespace_separated(input_string):
    return '  '.join(input_string.split()) == input_string.strip()

wordsfile = file("data/OEDmeaning.txt")
words = wordsfile.readlines()
words = [i.split('\n',1)[0] for i in words]

tmp = []
for i in words:
    if i == '' or i == " ":
        tmp.append(i)
    elif i[-1] == ' ':
        tmp.append(i)

tmp.sort()
tmp.reverse()

for i in tmp:
    words.remove(i)

print len(words)
# 36665

options = ['prefix', 'abbr.', 'n.', 'adv.', 'naut.', 'adj.', 'v.', '-v.', '-adj.', 'predic.', 'suffix', 'gram.', '-prep.', '-n.', '-int.', 'var.', 'Abbr.', 'n.pl.', 'attrib.', 'colloq.', 'int.', 'past']

words1 = {}
for i in words[0:10]:
    j=0
    while i.split()[j] == i .split(' ')[j]:
        j=j+1
    words1[' '.join(i.split()[0:j])] = ' '.join(i.split()[j:len(i.split())])


# for i in words1:
#     if i.split()[1] not in options:
#         j=0
#         while i.split()[j] == i .split(' ')[j]:
#             j=j+1
#         i = [' '.join(i.split()[0:j]), ' '.join(i.split()[j:len(i.split())])]
#     else:
#         i = [' '.join(i.split()[0:1]), ' '.join(i.split()[1:len(i.split())])]

# for i in words:
#     if i == '' or i == " ":
#         words.remove(i)
# for i in words:
#     if i == '' or i == " ":
#         words.remove(i)
# for i in words:
#     if i == '' or i == " ":
#         words.remove(i)
        
# print len(words)
# tmp = []
# for j in range(len(words)) :
#     if words[j][-1] == ' ':
#         tmp.append(j)
# tmp.reverse()
# print tmp
# for i in tmp:
#     print words[i]

# print words[0:50]

# wordsfile = file("words.txt")
# words4 = wordsfile.readlines()
# words4 = [i.split('\n',1)[0] for i in words4]
#
# print 4 , len(words4)
#
# words2 = words[44:len(words)]
# words3 = []
#
# for i in words2:
#     if not (i[len(i)-1] == 's' and i[len(i)-2] == "'"):
#         words3.append(i)
#
# start = time.clock()
# for i in words3:
#     if i not in words4:
#         words4.append(i)
# end = time.clock()
#
# print end-start
# print 2 , len(words2)
# print 3 , len(words3)
# print 4 , len(words4)
#
# words4.sort()
#
# thefile = open('output.txt', 'w')
# for item in words4:
#     thefile.write("%s\n" % item)
# thefile.close()
