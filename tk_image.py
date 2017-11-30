from tkinter import *

window = Tk()
window.title('Image')

img = PhotoImage(file='python.gif')

label = Label(window, image=img, bg='yellow')

small_img = PhotoImage.subsample(img, x=2, y=2)

btn = Button(window, image=small_img)

