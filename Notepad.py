from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
root=Tk()

root.geometry("1600x900")

root.title("Notepad")

ta=Text(width=1600,height=900)

ta.pack()

def quit():
    a=''
    a=showwarning(title="Exit",message="Do You Want To Exit")
    if(a=='ok'):
        root.destroy()

def openfile():
    c=askopenfile(defaultextension=".txt")
    filename=c.name
    root.title(os.path.basename(filename)+ " - Notepad")
    f=open(filename,"r")
    ta.delete(1.0,END)
    ta.insert(1.0,f.read())
    f.close()

def savefile():
    c=asksaveasfile(initialfile="Untitled.txt",defaultextension=".txt")
    filename=c.name
    f=open(filename,"w")
    f.write(ta.get(1.0, END))
    f.close()
    root.title(os.path.basename(filename) + " - Notepad")

def newfile():
    root.title("Notepad")
    ta.delete(1.0,END)

def cut():
    ta.event_generate("<<Cut>>")
def copy():
    ta.event_generate("<<Copy>>")
def paste():
    ta.event_generate("<<Paste>>")

def info():
    showinfo(title="Information Box",message="Notepad Created by Kaushal Saraswat")







mymenu=Menu()

list1=Menu()

list1.add_command(label="New",command=newfile)

list1.add_command(label="Open",command=openfile)

list1.add_command(label="Save",command=savefile)

list1.add_command(label="Exit",command=quit)

mymenu.add_cascade(label="File",menu=list1)





list2=Menu()

list2.add_command(label="Cut",command=cut)

list2.add_command(label="Copy",command=copy)

list2.add_command(label="Paste",command=paste)

mymenu.add_cascade(label="Edit",menu=list2)

list3=Menu()

list3.add_command(label="About Notepad",command=info)

mymenu.add_cascade(label="Help",menu=list3)

root.config(menu=mymenu)

root.mainloop()

