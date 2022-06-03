import os
from tkinter import *

globalentry = ""


def create():
    os.popen("python userPlus.py")


def inter():
    os.popen("python intamdin.py")


def acc():
    os.popen("python change_acc.py")


def addmach():
    os.popen("python ajoutmach.py")


def choixcom():
    global globalentry
    win1 = Tk()
    win1.title("La tirelire magique ")
    win1.geometry("500x400")

    label = Label(win1, text='numero du port com', font=('Courrier', 27))
    label.pack(side=TOP)

    globalentry = Entry(win1, width=45)
    globalentry.pack(expand=YES)

    butt = Button(win1, text='changer le port', font=('Courrier', 20), command=tu)
    butt.pack(expand=YES, side=LEFT)

    win1.mainloop()


def tu():
    global globalentry
    f = open('config.txt', 'r')
    machinecom = f.readlines()
    machine = machinecom[0]
    print(machine)
    f.close()
    com = globalentry.get()
    f = open('config.txt', 'w')
    f.write(machine)
    f.close()
    f = open('config.txt', 'a+')
    f.write(com)
    f.close()


win = Tk()

win.title("La tirelire magique ")
win.geometry("600x258")
win.config(background='#00ffe0')

butuser = Button(win, text='créer un utilisateur', font=('Courrier', 20), bg='#00ffe0', command=create)
butuser.pack(anchor=NW, expand=YES)

butmachine = Button(win, text='ajouter une machine', font=('Courrier', 20), bg='#00ffe0', command=addmach)
butmachine.place(x=300, y=0)

butdata = Button(win, text='données utilisateur', font=('Courrier', 20), bg='#00ffe0', command=inter)
butdata.place(x=300, y=200)

butaccess = Button(win, text='changer les accès', font=('Courrier', 20), bg='#00ffe0', command=acc)
butaccess.place(x=0, y=200)

butcom = Button(win, text='paramétrer le port com', font=('Courrier', 20), bg='#00ffe0', command=choixcom)
butcom.place(x=150, y=100)

win.mainloop()
