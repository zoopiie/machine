import json


with open("main prog/config.txt", "r") as f:
    txt = f.readlines()

    opt = txt[1]

    print(opt)
    f.close()