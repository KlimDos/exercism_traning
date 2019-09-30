import re
import operator
import pprint

def count_letters(text: str):
    dict = {}
    text = text.lower()
    for i in text:
        try:
            new_value = int(dict.get(i))+1
            dict[i] = new_value
            #print ("try")
        except:
            dict[i] = 1
            #print ("exeption")
        #print(dict.get(i)) 
    return dict

def show_sorted(dict):
    v = max(dict.items(), key=operator.itemgetter(1))[0]
    return v
    

def sort(dict):
    v = sorted(dict.items())
    return v

#c = sort(count_letters('Text one more time this is the text'))
#print(show_sorted(c))

c1 = count_letters('Text one more time this is the text')
pre = 0
for key, value in c1.items():
    #print (f'key {key}, value {value}')
    if value > pre:
        print (pre)
        pre = value
        
    else:
        #c1.pop('key', None)
        print ('else')
        del c1[key]


pprint.pprint(c1)
##    if item.
#c2 = show_sorted(c1)
#print(c2)