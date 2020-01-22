from tkinter import *
import re
import tkinter .font as font
import sqlite3
import os
from tkinter import messagebox
interface=Tk()
interface.configure(bg='#48332F')
interface.title('ASSIGNMENT')
interface.geometry("400x300")

email=StringVar()
password=StringVar()


def register():
    interface.destroy()
    os.system('register.py')
def out():
    interface.destroy()

#buttons in interface    
    
def submit():
    j=0
    try:
        conn=sqlite3.connect('database.db')
        print("CONNECTED")
    except:
        print("DATABASE NOT CONNECTED")

    m=conn.execute("select Mail_Address,Password from data")
    mail=email.get()
    key=password.get()
    if(len(mail)==0 or len(key)==0):
        messagebox.showinfo("!!ERROR!!", "PLEASE FILL IN THE DATA")
        #obj.func_1()
    if ('@' not in mail):
        messagebox.showinfo("!!ERROR!!", "PLEASE PROVIDE A VALID MAIL ID")
        #obj.func_1()
    else:
        pass
    if(len(key)<6):
        messagebox.showinfo("!!ERROR!!","PLEASE ENSURE LENGTH OF PASSWORD(ATLEAST 6)")
        #obj.func_1()
    else:
        pass
    for i in m:
        if(mail in i[0]):
            if(key in i[1]):
                conn.commit()
                interface.destroy()                
                os.system('welcome.py')
            else:
                messagebox.showinfo("!!ERROR!!","PASSWORD IS INCORRECT")
        else:
            pass
Label(interface,text="EMAIL: ",font='cambria').place(x=10,y=100)
Entry(interface,textvar=email,font='cambria',bd=2).place(x=150,y=100)
Label(interface,text="PASSWORD: ",font='cambria').place(x=10,y=150)
Entry(interface,textvar=password,font='cambria',bd=2,show="*").place(x=150,y=150)


button1= Button(interface,text="LOGIN",padx=5,pady=5,command=submit,bg="white", fg="black").place(x=150,y=200) 

#button1.config(font=('helvetica', 20, 'underline italic'))
button2 = Button(interface,text="REGISTER",padx=5,pady=5,command=register,bg="white", fg="black").place(x=250,y=200)
#button2.config(font=('helvetica', 20, 'underline italic'))
button3= Button(interface,text="EXIT",command=out,bg="white", fg="black").place(x=360,y=10) 
interface.mainloop()
