import os
from tkinter import *


def create():
    os.popen("python machines.py")


def mach():
    win.destroy()
    os.popen("python choixma.py")


win = Tk()

win.title("La tirelire magique ")
win.geometry("600x258")
win.config(background='#00ffe0')

buta = Button(win, text='utiliser la machine', font=('Courrier', 20), bg='#00ffe0', command=create)
buta.pack(expand=YES)

bute = Button(win, text='paramétrer la machine', font=('Courrier', 20), bg='#00ffe0', command=mach)
bute.pack(expand=YES)

win.mainloop()
