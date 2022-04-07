methods = ['talk', 'book', 'think']

print('methods =',methods, '\n')

#1
print('#1')
first = methods[0]
last = methods[len(methods) - 1]

methods[0] = last
methods[len(methods) - 1] = first

print(methods)

methods = ['talk', 'book', 'think']


#2
print('\n#2')
newList = methods.copy()

newList[0] = methods[len(newList) - 1]
newList[len(newList) - 1] = methods[0]
methods = newList

print(methods)