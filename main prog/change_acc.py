from tkinter import *
from sqlcommand import execute
import json

with open("machfile.json", "r") as f:
    txt = json.load(f)
    option = txt["option"]
    client = txt["client"]
    f.close()

OptionList = option
cnc = ""


def setparametre(client):
    n = len(client)
    char = "("
    for i in range(n - 2):
        char = "%s%s%s" % (char, client[i], ", ")
    char = "%s%s%s" % (char, client[n - 1], ")")
    return char


def update():
    cc = cnc.get()
    var = variable.get()
    nm = nom.get()
    pm = prenom.get()
    execute("UPDATE client SET acc_{}='{}' WHERE nom='{}' AND prenom='{}'".format(var, cc, nm, pm))
    rt = Toplevel(win)
    rt.title('test')
    lab = Label(rt, text="données mise à jour", font=("Courrier", 27), fg='white', bg='#00ffe0')
    lab.pack()


client = setparametre(client)
win = Tk()

win.title("La tirelire magique ")
win.geometry("800x600")
win.config(background='#00ffe0')

variable = StringVar(win)
variable.set(OptionList[0])

label = Label(win, text='prenom', font=('Courrier', 27), bg='#00ffe0')
label.pack(side=TOP)

prenom = Entry(win, width=45)
prenom.pack(expand=YES)

label1 = Label(win, text='nom', font=('Courrier', 27), bg='#00ffe0')
label1.pack(side=TOP)

nom = Entry(win, width=45)
nom.pack(expand=YES)

optionmenu = OptionMenu(win, variable, *OptionList)
optionmenu.config(width=90, font=('Helvetica', 12))
optionmenu.pack(side=BOTTOM)

cnc = StringVar()
C2 = Checkbutton(win, text="autorisé à la machine", variable=cnc, onvalue="oui", offvalue="non", height=5,
                 width=20, bg='#00ffe0')
C2.pack()

but = Button(win, text='changer les droits', font=('Courrier', 20), bg='#00ffe0', command=update)
but.pack(expand=YES)

win.mainloop()
