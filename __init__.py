from tkinter import *
import sqlite3
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from sqlitegui import *

root =Tk()
root.title('Login portal for N.S.N COLLEGE OF ENGINEERING AND TECHNOLOGY ') 

def photo():
    load=Image.open('12.png')
    r=PhotoImage(load)
    photo = ImageTk.PhotoImage(file='12.png')
    label = Label(root,image=photo,width='10',height='20')
    label.pack()


def label(name,bgcolr,fgcolr,sid):
    label_1=Label(root,text=name,bg=bgcolr,fg=fgcolr,width='10',height='2')
    label_1.place(relx=5,rely=4)
    label_1.pack(side=sid,expand=YES,padx=5, pady=100)


def button(name,bgcol,fgcolr,sid):
    button_1=Button(root,text=name,bg=bgcol,fg=fgcolr,width='10',height='2')
    button_1.pack(side=sid,anchor=W,fill=X,expand=YES)

def entry(sid,bsid):
    entry_1=Entry(root)
    entry_2=Entry(root,show='*')
    entry_1.pack(side=sid,expand=YES, padx=5, pady=100)
    entry_2.pack(side=sid,expand=YES, padx=5, pady=100)
    def getLine():
        lineTxt_1 = str(entry_1.get())
        lineTxt_2 = str(entry_2.get())
        logName=str(entry_1.get())
        logPassword=str(entry_2.get())
        read_db(logName,logPassword)
        c.close()
        conn.close()
    button_2=Button(root,text='Log in',command=getLine)
    button_2.pack(side=bsid,anchor=W,fill=X,expand=YES)

def password(sid,bsid,txt):
    password_1=Entry(root,show='*')
    password_1.pack(side=sid)
    def passwordget():
        print("Password :"+password_1.get())
    button_3=Button(root,text=txt,command=passwordget)
    button_3.pack(side=bsid,anchor=W,fill=X,expand=YES)




