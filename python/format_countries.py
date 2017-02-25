import string
import sys
import json

wordsfile = file("data/countries.txt")
raw = wordsfile.readlines()
raw = [i.split('\n',1)[0] for i in raw]

countries={}

for i in raw:
    countries[i.split('|',1)[0]] = [i.split('|',1)[1]]
    
tmp = []

for i in countries:
    countries[i].append(countries[i][0])
    
countries['RU'][1] = "Russia"

for i in countries:
    if 'Antilles' in countries[i][0]:
        countries[i][1] = "Antilles"
    if 'Brunei' in countries[i][0]:
        countries[i][1] = "Brunei"
    if 'United Kingdom' in countries[i][0]:
        countries[i][1] = "Britain"
    if "Palestinian" in countries[i][0]:
        countries[i][1] = "Palestine"
    if "Viet" in countries[i][0]:
        countries[i][1] = "Vietnam"
    if "Moldova" in countries[i][0]:
        countries[i][1] = "Moldova"
    if "Macedonia" in countries[i][0]:
        countries[i][1] = "Macedonia"
    if "Svalbard" in countries[i][0]:
        countries[i][1] = "Svalbard"
    if "Falkland" in countries[i][0]:
        countries[i][1] = "Malvinas"
        countries[i][0] = "Falkland Islands"
    if "Micronesia" in countries[i][0]:
        countries[i][1] = "Micronesia"
    if "ivoire" in countries[i][0]:
        countries[i][1] = "Ivory Coast"
    if "Cocos" in countries[i][0]:
        countries[i][1] = "Keeling Islands"
        countries[i][1] = "Cocos Islands"
    if ("Congo" and "Democratic") in countries[i][0]:
        countries[i][1] = "Democratic Republic Of The Congo"
    if "Syrian" in countries[i][0]:
        countries[i][1] = "Syria"
    if "Korea" in countries[i][0]:
        if "Democratic" in countries[i][0]:
            countries[i][1] = "North Korea"
            continue
        countries[i][1] = "South Korea"
    if "Lao" in countries[i][0]:
        countries[i][1] = "Laos"
    if "Taiwan" in countries[i][0]:
        countries[i][1] = "Taiwan"
    if "Iran" in countries[i][0]:
        countries[i][1] = "Iran"
    if "vatican" in countries[i][0]:
        countries[i][1] = "Vatican"
        countries[i][0] = "Holy See"
    if "Libya" in countries[i][0]:
        countries[i][1] = "Libya"
    if "Lao" in countries[i][0]:
        countries[i][1] = "Laos"

for i in countries:
    foo=0
    bar=0
    for j in countries[i][0]:
        if j is " ":
            foo=foo+1
    countries[i].append(foo+1)
    countries[i].append(len(countries[i][0]))
    for j in countries[i][1]:
        if j is " ":
            bar=bar+1
    countries[i].append(bar+1)
    countries[i].append(len(countries[i][1]))

json.dump(countries, open("data/countriesOUT.txt",'w'))

# for i in tmp:
#     countries[i.split(', ',1)[0]] = countries[i]
#     countries[i.split(', ',1)[1] + " " + i.split(', ',1)[0]] = countries[i]
#     del countries[i]
#
# countries["Cocos Islands"] = countries["Cocos (keeling) Islands"]
# countries["Keeling Islands"] = countries["Cocos (keeling) Islands"]
# del countries["Cocos (keeling) Islands"]
# countries["Falkland Islands"] = countries["Falkland Islands (malvinas)"]
# countries["Malvinas"] = countries["Falkland Islands (malvinas)"]
# del countries["Falkland Islands (malvinas)"]
# countries["Holy See"] = countries['Holy See (vatican City State)']
# countries['Vatican City State'] = countries['Holy See (vatican City State)']
# del countries['Holy See (vatican City State)']

# for i in countries:
#     foo=0
#     for j in i:
#         if j is " ":
#             foo = foo + 1
#     countries[i].append(foo + 1)
#     countries[i].append(len(i))

# print len(countries)
#
# for i in countries:
#     print countries[i][0]


# x=range(len(raw))
# x.reverse()
#
# words=[]
#
# for i in raw:
#     if "  " not in i:
#         continue
#     words.append(i)
#
# oed = {'test':'entry'}
#
# for j in words:
#     for i in range(len(j)):
#         if j[i] == " " and j[i+1] == " ":
#             oed[j[0:i]] = j[i+2:len(j)]
#
# for i in oed:
