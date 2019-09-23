import re
import operator

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


c = show_sorted(count_letters('Text'))
print(c)
