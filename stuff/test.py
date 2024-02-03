dict = [{'country': 'usa','name' : 'nat','last': 'rob'}, {'country': 'mia','name' : 'pat','last': 'tobby'}]
templist = []
tempdict = {}
for i in dict:
    templist.append(i['name'])
    templist.append(i['last'])
    country = i['country']
    tempdict.update({country: templist})

print(tempdict)