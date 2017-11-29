from tkinter import *

import tkinter.messagebox as box

window = Tk()
window.title('Приложение')

def dialog():
    var = box.askyesno('Message Box', 'Начать?')

    if var == 1:
        box.showinfo('Yes Box', 'В процессе...')
    else:
        box.showwarning('No Box', 'Отмена...')

btn = Button(window, text='Click', command=dialog)
btn.pack(padx=150, pady=50)

window.mainloop()
