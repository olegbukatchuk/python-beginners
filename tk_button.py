from tkinter import *

window = Tk()

window.title('Приложение')

btn_end = Button(window, text='Закрыть', command=exit)

def tog():
    if window.cget('bg') == 'yellow':
        window.configure(bg='gray')
    else:
        window.configure(bg='yellow')

btn_tog = Button(window, text='Изменить', command=tog)

btn_end.pack(padx=150, pady=20)
btn_tog.pack(padx=150, pady=20)

window.mainloop()