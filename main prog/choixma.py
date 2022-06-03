from tkinter import *
import json


with open("machfile.json", "r") as f:
    txt = json.load(f)
    option = txt["option"]
    client = txt["client"]
    f.close()

OptionList = option
variable = 0
com = 0


def setparametre(clients):
    n = len(clients)
    char = "("
    for i in range(n - 2):
        char = "%s%s%s" % (char, clients[i], ", ")
    char = "%s%s%s" % (char, clients[n - 1], ")")
    return char


client = setparametre(client)


def choix():
    global variable, com
    clear_frame()

    win.selection_clear()
    variable = StringVar(win)
    variable.set(OptionList[0])

    optionmenu = OptionMenu(win, variable, *OptionList)
    optionmenu.config(width=90, font=('Helvetica', 12))
    optionmenu.pack(side=BOTTOM)

    label1 = Label(win, text='numéro du port COM', font=('Courrier', 27), bg='#00ffe0')
    label1.pack(side=TOP)

    com = Entry(win, width=45)
    com.pack(expand=YES)

    butt = Button(win, text='valider le choix', font=('Courrier', 20),
                  command=text)
    butt.pack(expand=YES)

    win.mainloop()


def text():
    global variable, com
    a = variable.get()

    cm = com.get()

    f = open('config.txt', 'w')
    f.write(a)
    f.close()
    f = open('config.txt', 'a+')
    f.write('\n')
    f.write(cm)
    f.close()


def password():
    a = mail.get()
    if (a == 'a'):
        choix()


def clear_frame():
   for widgets in win.winfo_children():
      widgets.destroy()


win = Tk()
win.title("La tirelire magique ")
win.geometry("500x400")

label = Label(win, text='password', font=('Courrier', 27))
label.pack(side=TOP)

mail = Entry(win, width=45)
mail.pack(expand=YES)

butt = Button(win, text='verif', font=('Courrier', 20), command=password)
butt.pack(expand=YES, side=LEFT)

win.mainloop()
