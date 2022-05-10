
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)


root.resizable(0, 0)

root.title("CALCULATOR")

def cButton(text, command):
    return Button(root, text=text, width=8, height=5, command=command)
def cDoubleButton(text):
    return Button(root, text=text, width=18, height=5)

expression = ''


ttk.Label(root, width= 5,padding=15, text='').grid()
display = Label(root, text= 'Do calculations!' if expression == '' else expression)
display.place(x=24, y=15)

def enter_number(number):
    display.config(text= expression + number)
    expression += number
    
    
     

# Input buttons
zero = cButton('0', enter_number('0'))
zero.grid(row=5, column=1)
one = cButton('1', enter_number('1'))
one.grid(row=4, column=0)
two = cButton('2', enter_number('2'))
two.grid(row=4, column=1)
three = cButton('3', enter_number('3'))
three.grid(row=4, column=2)
four = cButton('4', enter_number('4'))
four.grid(row=3, column=0)
five = cButton('5', enter_number('5'))
five.grid(row=3, column=1)
six = cButton('6', enter_number('6'))
six.grid(row=3, column=2)
seven = cButton('7', enter_number('7'))
seven.grid(row=2, column=0)
eight = cButton('8', enter_number('8'))
eight.grid(row=2, column=1)
nine = cButton('9', enter_number('9'))
nine.grid(row=2, column=2)


# Operations

sum = cButton('+')
sum.grid(row=1, column=3)
subt = cButton('-')
subt.grid(row=2, column=3)
divi = cButton('÷')
divi.grid(row=3, column=3)
mult = cButton('x')
mult.grid(row=4, column=3)

# Other operation buttons

resu = cButton('=')
resu.grid(row=5, column=3)

dot = cButton('.')
dot.grid(row=5, column=2)

clea = cDoubleButton('C')
clea.grid(row=1, column=0, columnspan=2)


ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop() 