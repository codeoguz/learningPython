#More on Tuples, Sets and Dictionaries
#Mutable, Immutable
mySet = {'great', 'awesome', 'magnificent'}
mySet.remove('great')

print(mySet)

""" myList = ['people', 'dogs']
myList[0] = 'humans'

print(myList) """

""" tup = ('people', 'dogs', 'cats')
 tup[0] = 'humans'

tup = ('dogs', 'cats')
print(tup) """

#Dictionary for loop

myDic = {'bad':'kotu', 'magnificent': 'sasali'}

""" print(myDic['bad']) """

for anahtar, isim in myDic.items():
    if(isim is 'sasali'):
        print(anahtar)
    

#Modules



