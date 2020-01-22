from tkinter import messagebox
from datetime import datetime
from tkinter import*
import smtplib, ssl

import tkinter

from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("hello.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

def out():
    date=datetime.now()
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email="enter your email"
    receiver_email= "enter"
    password3 ="enter your password"
    text= "Session Id is: "+str(date)
        
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password3)
        server.sendmail(sender_email, receiver_email, text)
    root.destroy()
    

root = Tk()
app = Window(root)
root.title("Welcome")
root.geometry("700x600")
#root.configure(bg='#FFFFCC')
Label(root,text="WELCOME HERE I AM YOUR HOST",font='cambria',padx=10,pady=10).place(x=222,y=100)
Button(root,text="END SESSION",command=out,bg="white", fg="black",padx=20,pady=20).place(x=300,y=460) 
root.mainloop()
