""" def sumNumbers(a, b):
    return a + b

class user:
    admin = False
    
    def __init__(self, name) -> None:
        self.name = name
    
    def shout(self, shout):
        print(f'{self.name}: {shout}')

    def numberSum(c,d):
        sumNumbers(c,d)
    
Kubilay = user('Kubilay')

Kubilay.shout(f'Emiiiir!! abe')

print(Kubilay.numberSum(15, 6)) """

#Computer [processor, graphicsCard, motherboard] [Draw[circle, rectangle, human], Compute[sum, subtract, divide, multiply]]

class Computer:
    def __init__(self, name, processor,motherboard = 'B450', graphicsCard = 'internalGPU') -> None:
        self.motherboard = motherboard
        self.graphicsCard = graphicsCard
        self.processor = processor
        self.name = name
    
    def drawCircle(self):
        print(f'Drew a circle on {self.name}')
        
myPC = Computer(name = 'Turbo',processor='Ryzen 3 3600')


myPC.drawCircle()