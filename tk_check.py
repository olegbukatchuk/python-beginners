from tkinter import *

import tkinter.messagebox as box

window = Tk()
window.title('Check Button')

frame = Frame(window)

var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()

book_1 = Checkbutton(frame, text='HTML5', variable=var_1, onvalue=1, offvalue=0)
book_2 = Checkbutton(frame, text='CSS3', variable=var_2, onvalue=1, offvalue=0)
book_3 = Checkbutton(frame, text='JS', variable=var_3, onvalue=1, offvalue=0)

def dialog():
    str = 'Your Choice:'

    if var_1.get() == 1:
        str += '\nHTML5 in easy steps'