from tkinter import *
from tkinter import filedialog as fd

root = Tk()
root.geometry('800x800')
root.title("Блокнот V1.0")


def opn():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    txt.insert(1.0, s)
    f.close()


def Save():
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    try:
        f = open(file_name, 'w')
        s = txt.get(1.0, END)
        f.write(s)
        f.close()
    except:
        print('frite not save')


def settings():
    win = Toplevel(root)
    win.geometry('250x250')
    win.title('Настрйка')
    btn = Button(win, text='ОК')
    btn.place(x=15,y=150)
    ent = Entry(win, width=20)
    ent.place(x=15,y=75)
    ent = Entry(win, width=20)
    ent.place(x=15, y=125)
    labl=Label(win,text="Изменить размер окна")
    labl.place(x=5,y=5)
    labl=Label(win,text="Изменить размер окна(x)")
    labl.place(x=5,y=55)
    labl=Label(win,text="Изменить размер окна(y)")
    labl.place(x=5,y=105)




def ext():
    exit()


mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Open', command=opn)
filemenu.add_command(label='Save', command=Save)
filemenu.add_command(label='Settings', command=settings)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=ext)

txt = Text(root)
txt.place(relwidth=1, relheight=1)

mainmenu.add_cascade(label='File', menu=filemenu)

root.mainloop()
