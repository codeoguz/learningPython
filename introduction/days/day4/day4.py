#read, write files

""" import os

print(os.getcwd())

def readFile(file):
    with open(file) as f:
        for line in f:
            print(line, end="")

readFile('LearningPython/days/day4/myFile.txt') """

#try, except

""" try:
    a = int(input('Ilk sayisiyi yaz:'))
    b = int(input('Ikinci sayisiyi yaz:'))
    
    print(f'Toplami: {a + b}')
except:
    print('Hata yaptin')
    pass """

""" from typing import final


try:
    4/0
    raise NameError

except NameError:
    print('Name Error Verdi')
except ZeroDivisionError:
    print('Sifira bolunemez')
finally:
    print('Sorgunun sonu') """

    
#classes



class Computer:
    def __init__(self, name, processor, motherboard = 'Asus', graphicsCard = 'internal'):
        self.name = name
        self.processor = processor
        self.motherBoard = motherboard
        self.graphicsCard = graphicsCard
    
    def drawCircle(_):
        print('Drew a circle')
    
    
myPC = Computer('Anka', 'Intel 12th Gen', graphicsCard='Rtx 3090')

print(myPC.graphicsCard)

myPC.drawCircle()