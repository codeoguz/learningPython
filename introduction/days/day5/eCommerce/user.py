from product import Product
import json

class User:
    def __init__(self, username) -> None:
        self.username = username
        self.id = generateID(10)
    def listallproducts():
        for product in allProducts:
            pass

    def serializeJSON(self):
        data = {'username': self.username, 'id':self.id}
        if self.__class__ is Trader:
            pass
        return json.dumps(data)
        
        
class Trader(User):
    def __init__(self, username) -> None:
        super().__init__(username)
        products = []
        
users = []

from random import randrange
def generateID(length):
    letters = 'abcdefg[hi\'jklmno,pr;stu]vyz'
    result = ''
    for i in range(length):
        result += letters[randrange(0, len(letters)-1)]
    return result

