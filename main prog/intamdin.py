from tkinter import *
import os
import json
from sqlcommand import fetchall, fetchone

with open("machfile.json", "r") as f:
    txt = json.load(f)
    opt = txt["option"]
    client = txt["client"]
    f.close()


def setparametre(clients):
    n = len(clients)
    char = "("
    for i in range(n - 2):
        char = "%s%s%s" % (char, clients[i], ", ")
    char = "%s%s%s" % (char, clients[n - 1], ")")
    return char


OptionList = opt
client = setparametre(client)
cnc = ""


def paye():
    nm = nom.get()
    pm = prenom.get()
    dt = date.get()
    var = variable.get()
    fetchone("UPDATE {} SET payé='oui' WHERE nom='{}' AND prenom='{}' AND jour='{}'".format(var, nm, pm, dt))
    rt = Toplevel(win)
    rt.title('test')
    lab = Label(rt, text='payement effectuer', font=("Courrier", 27), fg='white', bg='#00ffe0')
    lab.pack()


def recup():
    nm = nom.get()
    pm = prenom.get()
    dt = date.get()
    var = variable.get()
    getsql = fetchall("SELECT nom, prenom, jour, temps, payé FROM {} WHERE nom='{}' AND prenom='{}' AND jour='{}'"
                      .format(var, nm, pm, dt))
    for i in range(len(getsql)):
        if i == 0:
            f = open('data.txt', 'w')
            f.write(str(getsql[i])+'\n')
            f.close()
        else:
            f = open('data.txt', 'a')
            f.write(str(getsql[i])+'\n')
            f.close()
    getsql = fetchone("SELECT SUM(temps) AS temps_total FROM {} WHERE nom='{}' AND prenom='{}' AND jour='{}'"
                      .format(var, nm, pm, dt))
    f = open('data.txt', 'a')
    f.write("il y a "+str(getsql[0]) + " minutes sélectionnées" + '\n')
    f.close()
    os.popen("data.txt")


def totalutil():
    nm = nom.get()
    pm = prenom.get()
    dt = date.get()
    var = variable.get()
    getsql = fetchone("SELECT SUM(temps) AS temps_total FROM {} WHERE nom='{}' AND prenom='{}' AND jour='{}'"
                      " AND payé='---'".format(var, nm, pm, dt))
    rt = Toplevel(win)
    rt.title('test')
    Label(rt, text="il y a {} minute impayé".format(getsql[0]), font=("Courrier", 27), fg='white', bg='#00ffe0').pack()


win = Tk()

win.title("La tirelire magique ")
win.geometry("800x600")
win.config(background='#00ffe0')

variable = StringVar(win)
variable.set(OptionList[0])

opt = OptionMenu(win, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side=BOTTOM)

label = Label(win, text='prenom', font=('Courrier', 27), bg='#00ffe0')
label.pack(side=TOP)

prenom = Entry(win, width=45)
prenom.pack(expand=YES)

label1 = Label(win, text='nom', font=('Courrier', 27), bg='#00ffe0')
label1.pack(side=TOP)

nom = Entry(win, width=45)
nom.pack(expand=YES)

label3 = Label(win, text='date (année-mois-jour)', font=('Courrier', 27), bg='#00ffe0')
label3.pack(side=TOP)

date = Entry(win, width=45)
date.pack(expand=YES)

pay = StringVar()

but = Button(win, text='enregistrer payement', font=('Courrier', 20), bg='#00ffe0', command=paye)
but.pack(expand=YES)

butr = Button(win, text='récuperer les données', font=('Courrier', 20), bg='#00ffe0', command=recup)
butr.pack(expand=YES)

butn = Button(win, text='afficher le total d\'heure non payé', font=('Courrier', 20), bg='#00ffe0', command=totalutil)
butn.pack(expand=YES)

win.mainloop()
