from tkinter import *
from sqlcommand import execute
import json


with open("machfile.json", "r") as f:
    txt = json.load(f)
    option = txt["option"]
    client = txt["client"]
    f.close()


def add():
    option.append(mach.get())
    machine = "%s%s" % ("acc_", mach.get())
    client.append(machine)
    print("i do ")
    print(option, client)
    data = {"option": option,
            "client": client}
    with open('machfile.json', 'w') as f:
        json.dump(data, f)
    execute("ALTER TABLE client ADD {} VARCHAR(3)".format(machine))
    execute("CREATE TABLE {} (temps INTtemps INT(11) ,jour VARCHAR(20), ref VARCHAR(4), nom VARCHAR(20),"
            " prenom VARCHAR(20), payé VARCHAR(3))".format(mach.get()))
    rt = Toplevel(win)
    Label(rt, text='nouvelle machine ajouté', font=25).pack()


win = Tk()

win.title("La tirelire magique ")
win.geometry("500x300")
win.config(background='#00ffe0')

label = Label(win, text='nom de la nouvelle machine ', font=('Courrier', 27), bg='#00ffe0')
label.pack(side=TOP)

mach = Entry(win, width=45)
mach.pack(expand=YES)

but = Button(win, text='ajouter la machine', font=('Courrier', 20),
             bg='#00ffe0', command=add)
but.pack(expand=YES)


win.mainloop()
