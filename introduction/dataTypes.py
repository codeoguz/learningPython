# Deque lists
""" from collections import deque
import queue

queue = deque (['Emir', 'Kubilay', 'Oguz', 'Omer'])

for i in range(1000):
    queue.append('Kaan')
    print(queue)

while len(queue) > 0:
    queue.popleft()
    print(queue)
        
print('The status of the list', queue) """



from random import randrange
#Dictionaries
""" user = {'name': 'Omer', 'age': 29}

def createUsers(number):
    letters = 'asdfghjklzxcvbnmn'
    userList = []
    for i in range(number):
        name = ''
        userAge = randrange(16, 99)
        for a in range(5):
            randNumber = randrange(len(letters))
            letter = letters[randNumber]
            name += letter
        userList.append({'name': name, 'age': userAge})
    return userList
myList = createUsers(100)

print([x for x, a in myList]) """



#Tuples
t = 'kaan', 'taha', 'faruk'
nested = (t ('banana', 'apple'), 'pc', 'mac', 'computer')

print(nested)



#Sets
a = set('abahreM')
basket =  {'banana', 'pinapple', 'apple', 'orange'}

'apple' in basket
