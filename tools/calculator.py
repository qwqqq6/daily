# 计算器
from tkinter import *

calculator = Tk()
calculator.title('计算器')


equ = StringVar()
equ.set('0')


def clear():
    equ.set('0')


def backspace():
    equ.set(equ.get()[0:-1])


def calculation():
    equ.set(eval(equ.get()))


def add(c):
    ver = equ.get()
    if ver == '0':
        equ.set(c)
    else:
        equ.set(ver + c)


label = Label(calculator, width=25, height=2, textvariable=equ, relief='groove', anchor=SE)
label.grid(row=0, column=0, columnspan=4)
Button(calculator, width=5, text='C', command=clear).grid(row=1, column=0)
Button(calculator, width=5, text='DEL', command=backspace).grid(row=1, column=1)
Button(calculator, width=5, text='%', command=lambda: add('%')).grid(row=1, column=2)
Button(calculator, width=5, text='/', command=lambda: add('/')).grid(row=1, column=3)
Button(calculator, width=5, text='7', command=lambda: add('7')).grid(row=2, column=0)
Button(calculator, width=5, text='8', command=lambda: add('8')).grid(row=2, column=1)
Button(calculator, width=5, text='9', command=lambda: add('9')).grid(row=2, column=2)
Button(calculator, width=5, text='*', command=lambda: add('*')).grid(row=2, column=3)
Button(calculator, width=5, text='4', command=lambda: add('4')).grid(row=3, column=0)
Button(calculator, width=5, text='5', command=lambda: add('5')).grid(row=3, column=1)
Button(calculator, width=5, text='6', command=lambda: add('6')).grid(row=3, column=2)
Button(calculator, width=5, text='-', command=lambda: add('-')).grid(row=3, column=3)
Button(calculator, width=5, text='1', command=lambda: add('1')).grid(row=4, column=0)
Button(calculator, width=5, text='2', command=lambda: add('2')).grid(row=4, column=1)
Button(calculator, width=5, text='3', command=lambda: add('3')).grid(row=4, column=2)
Button(calculator, width=5, text='+', command=lambda: add('+')).grid(row=4, column=3)
Button(calculator, width=12, text='0', command=lambda: add('0')).grid(row=5, column=0, columnspan=2)
Button(calculator, width=5, text='.', command=lambda: add('.')).grid(row=5, column=2)
Button(calculator, width=5, text='=', command=calculation).grid(row=5, column=3)


calculator.mainloop()