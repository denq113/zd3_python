from tkinter import *

def str_to_pl():
    try:
        s = int(ent1.get())
        e = int(ent2.get())
        d = s + e
        lab['text'] = str(d)
    except ValueError:
        lab['text'] = "Ошибка"

def str_to_min():
    try:
        s = int(ent1.get())
        e = int(ent2.get())
        d = s - e
        lab['text'] = str(d)
    except ValueError:
        lab['text'] = "Ошибка"

def str_to_um():
    try:
        s = int(ent1.get())
        e = int(ent2.get())
        d = s * e
        lab['text'] = str(d)
    except ValueError:
        lab['text'] = "Ошибка"

def str_to_raz():
    try:
        s = int(ent1.get())
        e = int(ent2.get())
        if e == 0:
            lab['text'] = "Ошибка: деление на 0"
        else:
            d = s / e
            lab['text'] = str(d)
    except ValueError:
        lab['text'] = "Ошибка"

root = Tk()
ent1 = Entry(width=20)
ent2 = Entry(width=20)
but1 = Button(text="+", width=10, command=str_to_pl)
but2 = Button(text="-", width=10, command=str_to_min)
but3 = Button(text="*", width=10, command=str_to_um)
but4 = Button(text="/", width=10, command=str_to_raz)
lab = Label(width=10, bg='white', fg='black')

ent1.pack()
ent2.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
lab.pack()
root.mainloop()