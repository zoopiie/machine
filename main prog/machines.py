from tkinter import *
from sqlcommand import fetchone, execute
import serial
from time import sleep
from threading import Timer
from datetime import *
from random import *


with open("config.txt", "r") as f:
    txt = f.readlines()
    com = txt[1]
    machine = txt[0]
    f.close()


acc = "%s%s" % ("acc_", machine)
ser = serial.Serial(com, 9600)
rfidscanned = ""
complement = []
ref = ""
varalim = 8
date = ""


def refutil():
    global date, machine, ref
    date = datetime.today().strftime('%Y-%m-%d')
    ref = "%s%s%s%s" % (
        randint(0, 9),
        randint(0, 9),
        randint(0, 9),
        randint(0, 9))
    getsql = fetchone("SELECT * FROM {} WHERE ref='{}'".format(machine, ref))
    if getsql != None:
        refutil()


def decodage():
    global rfidscanned, complement
    aux = ser.readline()
    rfidscanned = ""
    complement = []
    for s in aux:
        d = chr(s)
        complement.append(d)
    if len(complement) > 8:
        for i in range(0, 8):
            f = complement[i]
            rfidscanned = "%s%s" % (rfidscanned, f)


def lectureSerie():
    if ser.inWaiting():
        decodage()
        sleep(1)
    Timer(1, verifacces).start()


def verifacces():
    global rfidscanned, complement
    butr.config(text="en cours")
    if len(complement) != 10:
        lectureSerie()
    else:
        butr.config(text="scan rfid")
        b = rfidtst(rfidscanned)
        complement = []
        if b != None:
            utilisationmachine(rfidscanned)
        else:
            rt = Toplevel(win)
            rt.title('test')
            lab = Label(rt, text='vous n\'avez pas les droits', font=("Courrier", 27), fg='white', bg='red')
            lab.pack()


def rfidtst(rfid):
    b = fetchone("SELECT * FROM client WHERE rfid='{}' AND {}='oui'".format((rfid, acc)))
    return b


def poweron():
    global varalim
    varalim = 0
    name = ligne[0]
    surname = ligne[1]
    refutil()
    set = (1, date, ref, name, surname, '---')
    execute("INSERT INTO {} (temps, jour, ref, nom, prenom, payé) VALUES ".format(machine, set))
    ser.write(b'1/r/n')
    compteur()


def poweroff():
    global varalim
    varalim = 2
    ser.write(b'2/r/n')
    rt = Tk()
    buton.config(bg='#00ffe0')
    rt.title('test')

    lab = Label(rt, text='extinction en cours', font=("Courrier", 27), fg='white', bg='red')
    lab.pack()

    rt.mainloop()


def utilisationmachine(rfid):
    global ligne, buton
    ligne = fetchone("SELECT * FROM client WHERE rfid='{}'".format(rfid))
    name = ligne[0]
    surname = ligne[1]

    rt = Toplevel(win)
    rt.title('test')
    rt.geometry('600x400')
    rt.config(background='#00ffe0')
    lab = Label(rt, text="Bienvenue {} {}".format(surname, name), font=("Courrier", 35), fg='white', bg='#00ffe0')
    lab.pack()
    buton = Button(rt, text='demarrer', font=('Courrier', 20), bg='#00ffe0', command=poweron)
    buton.pack(expand=YES, side=LEFT)
    bute = Button(rt, text='eteindre', font=('Courrier', 20), bg='#00ffe0', command=poweroff)
    bute.pack(expand=YES, side=RIGHT)


def compteur():
    global varalim
    if varalim == 0:
        timer = 0
        while timer < 60:
            sleep(1)
            timer += 1
        getsql = fetchone("SELECT * FROM {} WHERE ref ='{}'".format(machine, ref))
        minute = getsql[0] + 1
        execute("UPDATE {} SET temps={} WHERE ref='{}'".format(machine, minute, ref))
        Timer(0.1, compteur).start()
    else:
        rt = Toplevel(win)
        rt.title('test')
        Label(rt, text='arret de la machine', font=("Courrier", 30), fg='white', bg='red').pack()


win = Tk()

win.title("La tirelire magique ")
win.geometry("400x300")
win.config(background='#00ffe0')
butr = Button(win, text='rfid scan', font=('Courrier', 20), bg='#00ffe0', command=verifacces)
butr.pack(expand=YES)
win.mainloop()
