from tkinter import *
from sqlcommand import execute, fetchone
import serial
from time import sleep
from threading import Timer
import random
import json

with open("machfile.json", "r") as f:
    txt = json.load(f)
    option = txt["option"]
    client = txt["client"]
    f.close()


with open("config.txt", "r") as f:
    txt = f.readlines()
    com = txt[1]
    f.close()


ser = serial.Serial(com, 9600)
rfid = ""
complement = []
lenoption = len(option)


def setparametre(clients):
    n = len(clients)
    char = "("
    for i in range(n - 2):
        char = "%s%s%s" % (char, clients[i], ", ")
    char = "%s%s%s" % (char, clients[n - 1], ")")
    return char


client = setparametre(client)


def createline():
    global rfid

    rfidtest()
    pm = prenom.get()
    nm = nom.get()

    user = (nm, pm, rfid, cnc.get(), laser.get())
    if lenoption >= 3:
        user = (nm, pm, rfid, cnc.get(), laser.get(), var3.get())
    if lenoption >= 4:
        user = (nm, pm, rfid, cnc.get(), laser.get(), var3.get(), var4.get())
    if lenoption >= 5:
        user = (nm, pm, rfid, cnc.get(), laser.get(), var3.get(), var4.get(), var5.get())
    if lenoption >= 6:
        user = (nm, pm, rfid, cnc.get(), laser.get(), var3.get(), var4.get(), var5.get(), var6.get())
    if lenoption >= 7:
        user = (nm, pm, rfid, cnc.get(), laser.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get())
    if lenoption >= 8:
        user = (nm, pm, rfid, cnc.get(), laser.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(),
                var8.get())
    if lenoption >= 9:
        user = (nm, pm, rfid, cnc.get(), laser.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(),
                var8.get(), var9.get())
    if lenoption >= 10:
        user = (nm, pm, rfid, cnc.get(), laser.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(),
                var8.get(), var9.get(), var10.get())

    execute("INSERT INTO client {} VALUES {}".format(client, user))
    rot = Toplevel(win)
    Label(rot, text="utilisateur crée", font=(" ", 27)).pack()


def decryptage():
    global rfid, complement
    aux = ser.readline()
    rfid = ""
    complement = []
    for j in aux:
        d = chr(j)
        complement.append(d)
    if len(complement) > 8:
        for i in range(0, 8):
            rfid = "%s%s" % (rfid, complement[i])


def lectureserie():
    global complement
    if ser.inWaiting():
        decryptage()
        global rfid
        sleep(1)
    Timer(1.0, lecturerifd()).start()


def lecturerifd():
    global rfid, complement
    butr.config(text="en cours")
    if len(complement) != 10:
        lectureserie()
    else:
        butr.config(text="scan rfid")
        ser.write(b'1/r/n')
        complement = []
        root = Toplevel(win)
        label = Label(root, text=rfid, font=(' ', 27), bg='red', fg='white')
        label.pack(side=TOP)


def rfidnew():
    newchar = ""
    for i in range(4):
        rand = random.randint(0, 255)
        if rand < 16:
            rand = hex(rand)[2:]
            rand = "%s%s" % ("0", rand)
        else:
            rand = hex(rand)[2:]
        newchar = "%s%s" % (newchar, rand)
    d = rfidget(newchar)
    if d != None:
        rfidnew()
    else:
        rt = Toplevel(win)
        rt.title('test')
        lab = Label(rt, text=newchar, font=("Courrier", 27), fg='white', bg='red')
        lab.pack()
    return newchar


def rfidget(rfid):
    get = fetchone("SELECT * FROM client WHERE rfid='{}'".format(rfid))
    return get


def rfidtest():
    get = fetchone("SELECT * FROM client WHERE rfid='{}'".format(rfid))
    if get != None:
        rt = Toplevel(win)
        rt.title('test')
        lab = Label(rt, text='rfid deja existant', font=("Courrier", 205), fg='white', bg='red')
        lab.pack()
    return get


win = Tk()

win.title("La tirelire magique ")
win.geometry("1920x900")
win.config(background='#00ffe0')

label = Label(win, text='prenom', font=('Courrier', 27), bg='#00ffe0')
label.pack(side=TOP)

prenom = Entry(win, width=45)
prenom.pack(expand=YES)

label1 = Label(win, text='nom', font=('Courrier', 27), bg='#00ffe0')
label1.pack(side=TOP)

nom = Entry(win, width=45)
nom.pack(expand=YES)

cnc = StringVar()
laser = StringVar()
C1 = Checkbutton(win, text="autorisé à la cnc", variable=cnc, onvalue="oui", offvalue="non", height=5, width=20,
                 bg='#00ffe0')
C2 = Checkbutton(win, text="autorisé au laser", variable=laser, onvalue="oui", offvalue="non", height=5, width=20,
                 bg='#00ffe0')
C2.pack()
C1.pack()


if lenoption >= 3:
    var3 = StringVar()
    C3 = Checkbutton(win, text="autorisé a {}".format(option[2]), variable=var3,
                     onvalue="oui", offvalue="non", height=5,
                     width=20, bg='#00ffe0')
    C3.place(x=100, y=400)
if lenoption >= 4:
    var4 = StringVar()
    C4 = Checkbutton(win, text="autorisé a {}".format(option[3]), variable=var4,
                     onvalue="oui", offvalue="non", height=5,
                     width=20, bg='#00ffe0')
    C4.place(x=300, y=400)
if lenoption >= 5:
    mc = "%s%s" % ("autorisé a 3", option[4])
    var5 = StringVar()
    C5 = Checkbutton(win, text="autorisé a {}".format(option[4]), variable=var5,
                     onvalue="oui", offvalue="non", height=5,
                     width=20, bg='#00ffe0')
    C5.place(x=100, y=450)
if lenoption >= 6:
    var6 = StringVar()
    C6 = Checkbutton(win, text="autorisé a {}".format(option[5]), variable=var6,
                     onvalue="oui", offvalue="non", height=5,
                     width=20, bg='#00ffe0')
    C6.place(x=300, y=450)
if lenoption >= 7:
    var7 = StringVar()
    C7 = Checkbutton(win, text="autorisé a {}".format(option[6]), variable=var7,
                     onvalue="oui", offvalue="non", height=5,
                     width=20, bg='#00ffe0')
    C7.place(x=100, y=500)
if lenoption >= 8:
    var8 = StringVar()
    C8 = Checkbutton(win, text="autorisé a {}".format(option[7]), variable=var8,
                     onvalue="oui", offvalue="non", height=5,
                     width=20, bg='#00ffe0')
    C8.place(x=300, y=500)
if lenoption >= 9:
    var9 = StringVar()
    C9 = Checkbutton(win, text="autorisé a {}".format(option[8]), variable=var9,
                     onvalue="oui", offvalue="non", height=5,
                     width=20, bg='#00ffe0')
    C9.place(x=100, y=550)
if lenoption >= 10:
    var10 = StringVar()
    C10 = Checkbutton(win, text="autorisé a {}".format(option[9]), variable=var10, onvalue="oui", offvalue="non",
                      height=5, width=20, bg='#00ffe0')
    C10.place(x=300, y=550)


but = Button(win, text='créer utilisateur', font=('Courrier', 20), bg='#00ffe0', command=createline)
but.pack(expand=YES)

butr = Button(win, text='scan rfid', font=('Courrier', 20), bg='#00ffe0', command=lecturerifd)
butr.pack(expand=YES)

butn = Button(win, text='rfid new', font=('Courrier', 20), bg='#00ffe0', command=rfidnew)
butn.pack(expand=YES, side=LEFT)

butt = Button(win, text='rfid test', font=('Courrier', 20), bg='#00ffe0', command=rfidtest)
butt.pack(expand=YES, side=LEFT)

win.mainloop()
