from tkinter import *

import tkinter.messagebox as box

window = Tk()
window.title('Radio Button')

frame = Frame(window)
book = StringVar()

radio_1 = Radiobutton(frame, text='HTML5', variable=book, value='HTML5 in easy steps')
radio_2 = Radiobutton(frame, text='CSS3', variable=book, value='CSS3 in easy steps')
radio_3 = Radiobutton(frame, text='JS', variable=book, value='JavaScript in easy steps')

Radio_1.select()

def dialog():
    