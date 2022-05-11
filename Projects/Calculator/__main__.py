
from audioop import reverse
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import onclick, right

root = Tk()
frm = ttk.Frame(root, padding=10)


root.resizable(0, 0)

root.title("CALCULATOR")

def cButton(text, myCommand, width = 10):
    return tkinter.Button(root, text=text, width=width, height=5, command=myCommand)
def cDoubleButton(text):
    return Button(root, text=text, width=18, height=5)

expression = ['', '', '']


# This will evaluate expression[] and output something like '5 + 4'
# First element represents operation, second is the first number and the last one is the second number
def returnDisplay():
    if expression[0] + expression[1] + expression[2] == '':
        return 'Do calculations!'
    elif expression[1] is '' and expression[0] is '':
        return expression[1]
    else:
        return f'{expression[1]} {expression[0]} {expression[2]}'


ttk.Label(root, width= 5,padding=15, text='').grid()
display = Label(root, text= returnDisplay(), justify='right')
display.grid(column=0, row=0, columnspan=4)


def enter_number(number, expression = expression):
    display.config(textvariable= expression[0] + number)
    expression[0] += number
    print(expression)

def set_operation(oper):
    expression[0] = oper
    


# Input buttons

zero = cButton('0', enter_number('0'))
zero.grid(row=5, column=1)

one = cButton('1', enter_number('1'))
one.grid(row=4, column=0)

two = cButton('2', enter_number('2'))
two.grid(row=4, column=1)

thre = cButton('3', enter_number('3'))
thre.grid(row=4, column=2)

four = cButton('4', enter_number('4'))
four.grid(row=3, column=0)

five = cButton('5', enter_number('5'))
five.grid(row=3, column=1)

six = cButton('6', enter_number('6'))
six.grid(row=3, column=2)

seve = cButton('7', enter_number('7'))
seve.grid(row=2, column=0)

eigh = cButton('8', enter_number('8'))
eigh.grid(row=2, column=1)

nine = cButton('9', enter_number('9'))
nine.grid(row=2, column=2)



# Operations

sum = cButton('+', set_operation('+'))
sum.grid(row=1, column=3)
subt = cButton('-', set_operation('-'))
subt.grid(row=2, column=3)
divi = cButton('÷', set_operation('÷'))
divi.grid(row=3, column=3)
mult = cButton('x', set_operation('x'))
mult.grid(row=4, column=3)

# Other operation buttons

""" resu = cButton('=')
resu.grid(row=5, column=3)

dot = cButton('.')
dot.grid(row=5, column=2)

clea = cDoubleButton('C')
clea.grid(row=1, column=0, columnspan=2) """


ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop() 