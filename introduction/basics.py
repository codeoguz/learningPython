''' Python Class '''

#]Numbers(int, float), Strings, Lists

'''
myNumber = 1.5
myString = 'Ömer'

employees = ['Oguz', 'Omer', 'Emir']
 
copyEmployees = employees.copy()
copyEmployees[0] = employees[len(employees) - 1]
copyEmployees[len(copyEmployees) - 1] = employees[0]

print(copyEmployees)
'''



# letters[2:4] = ['C', 'D', 'E', 'F']

# print(letters)

#]if, elif, else

# while True:
    # name = input('Isminig gir: ')
    # if name == 'omer':
        # print('Codeadin Ceosusun')
    # elif name == 'oguz':
        # print('arapca ogreniyosun')
    # else:
        # print('Codead')

#]for, range

# for(int i = 0; i < 10; i++){}

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# for a in letters:
    # if a == 'd':
        # break
    # print('Karakter ' + a)
    
    
    


#]while




#]break, continue




#]match

isim = 'emir'

if isim == 'kaan':
    print('hicbisey')
elif isim == 'emir':
    print('emir')


match isim:
    case 'kaan':
        print('hicbisey')
    case 'emir':
        print('hicbisey')
