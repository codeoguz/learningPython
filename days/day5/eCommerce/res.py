def p(content):
    return f"""
    _________________________________________
    -----------------------------------------
    -
    -
    {content}
    -
    -
    __________________________________________
    """

from user import *
import json
import os
#Add users
oguz = User('codeoguz')
omer = User('byyaman')
emir = Trader('emtaha')

users.append(oguz.serializeJSON())
users.append(omer.serializeJSON())
users.append(emir.serializeJSON())

path = 'database'
if not os.path.exists(path):
    os.makedirs(path)


jsonString = json.dumps(users)
jsonFile = open('data.json', 'w')
jsonFile.write(jsonString)  
jsonFile.close()