#ECommerce System
""" 
It consists of two sides(traders, customers), traders must log in to do actions
Main functions:
- Log in
- Display products
    - One by one
    - As list

For customers:
- Shopping bag
- Buy product

For traders:
- Create product
- Update product

"""

from user import User, Trader, users
from res import *

user = None

while user is None:
    option = input(
        '''
        What do you want?
        [1] Login
        [2] Register
        [3] Info
        :''')
    if option is '1':
        username = input('Enter username: ')
        for loopUser in users:
            if loopUser.username == username:
                user = loopUser
        if user is None:
            print(p('There is no such user :( Try again'))
    elif option is '2':
        #Register user by saving info to data.json
        username = input('Enter username: ')
        newUser = User(username)
        
        jsonString = json.dumps(newUser.serializeJSON())
        jsonFile = open('data.json', 'w')
        jsonFile.write(jsonString)
        jsonFile.close()
    
            
print(p(f'Welcome {user.username}!'))

userOption = input(p(
    f'''
    What do you want me to do?
    [1] Display products
    [2] Display shopping bag
    [3] Display your account
    '''))

if(userOption is '1'):
    pass
elif(userOption is '2'):
    pass
elif(userOption is '3'):
    print(p(
            f'''
            Username: {user.username}
            UserID: {user.id}
            '''
        ))