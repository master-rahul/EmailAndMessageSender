from tkinter import messagebox
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from array import *
from tkinter import*
import smtplib, ssl
import string
import sqlite3
import tkinter
import os
import math
import re
import time 
from time import sleep 
from sinchsms import SinchSMS

a = 3
if a == 3:
    a = 0
else:
    a = 3
print('the value of __name__ in A is %s' % __name__)
if __name__ == '__main__':
    print ('This statement will be executed only if this script is called directly')

interface=Tk()
interface.title("REGISTER")
interface.geometry("600x540")
interface.configure(bg='#FFFFCC')
first_name=StringVar()
second_name=StringVar()
gender=IntVar()
number=StringVar()
mail=StringVar()
password1=StringVar()
password2=StringVar()


regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
class A:
    def func_1(self):
        interface.destroy()
        os.system('register.py')
obj=A()

def sendSMS(): 
  
    #register at sinch sms and enter your own details
    num = 'enter your phone number'
    appkey = 'use the app key given'
    appsecret = 'enter the appsecret'
  
    # enter the message to send 
    message1 = "Welcome "+name_1+" "+name_2+",\n"+"Email: "+email+"\n"+"Paaword: "+password 
  
    c = SinchSMS(appkey, appsecret) 
    print("Send'%s' to %s" % (message1, num)) 
  
    response = client.send_message(num, message1) 
    message_id = response['messageId'] 
    response = client.check_status(message_id) 
    while response['status'] != 'Successful': 
        print(response['status']) 
        time.sleep(1) 
        response = client.check_status(message_id)   
    print(response['status'])
    
def check(email):  
    if(re.search(regex,email)):  
        print("Valid Email")  
    else:  
        messagebox.showinfo("!!ERROR!!","PLEASE ENTER A VALID phone number")
        obj.func_1()

def submit():
    name_1=first_name.get()
    name_2=second_name.get()
    gen=gender.get()
    phone=number.get()
    email=mail.get()
    password=password1.get()
    if len(first_name.get()) <= 2 or len(second_name.get()) <= 2 or gender.get() == 0 or len(mail.get()) == 0 or len(password1.get()) == 0 or len(password2.get()) == 0 or password2.get()!= password1.get():
        messagebox.showinfo("!!ERROR!!", "PLEASE CHECK INPUT DATA OR CHECK THE PASSWORD")
        obj.func_1()
    else:
        pass
    check(email)
    if len(phone)< 10 or len(phone)>10:
        messagebox.showinfo("!!ERROR!!", "ENETR VALID PHONE NUMBER")
        obj.func_1()
    if(len(password)<6):
        messagebox.showinfo("!!ERROR!!","PLEASE ENSURE LENGTH OF PASSWORD(ATLEAST 6)")
        obj.func_1()
    else:
        if(gen == 1):
            gen='MALE'
        else:
            gen='FEMALE'
        try:
            conn = sqlite3.connect("database.db")
            print("DATABASE CONNECTED")
        except Error as e:
            print(e)
        #conn.execute("create table data(First_Name varchar(50),Second_Name varchar(50),Gender varchar(6),Phone_Number number(10),Mail_Address varchar(50),Password varchar(50));")
        print(type(name_1))
        print(name_1)
        date= datetime.now()
        conn.execute("insert into data(First_Name,Second_Name,Gender,Phone_Number,Mail_Address,Password,Time)values(?,?,?,?,?,?,?)",(name_1,name_2,gen,phone,email,password,date))
        conn.commit()
        file = open("send.txt","w") 
        file.write("Your Information\n") 
        file.write("Name: "+name_1+" "+name_2+"\n") 
        file.write("Phone: "+ phone+"\n") 
        file.write("Email: "+ email+"\n")
        file.write("Password: "+ password+"\n") 
        file.write("Session: "+ str(date)+"\n")
        file.close()
        sender_email = "put your own email id"
        receiver_email = email
        msg = MIMEMultipart() 
        msg['From'] = sender_email 
        msg['To'] = receiver_email 
        msg['Subject'] = "master-rahul welcomes you" 
        body = "Your Information\n"
        msg.attach(MIMEText(body, 'plain'))  
        filename = "send.txt"
        attachment = open("C:\\Users\\maste\\Desktop\\ASSIGNMENT\\send.txt", "rb") 
        p = MIMEBase('application', 'octet-stream') 
        p.set_payload((attachment).read()) 
        encoders.encode_base64(p) 
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)  
        msg.attach(p) 
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        
        password3 ="put your own email password"
        text =msg.as_string()

        
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password3)
            server.sendmail(sender_email, receiver_email, text)
        sendSMS()
        interface.destroy()
        
        os.system('main.py')
       
Label(interface,text="FIRST NAME",font='cambria').place(x=120,y=100)
Entry(interface,textvar=first_name,font='cambria',bd=2).place(x=320,y=100)
Label(interface,text="SECOND NAME",font='cambria').place(x=120,y=150)
Entry(interface,textvar=second_name,font='cambria',bd=2).place(x=320,y=150)
Radiobutton(interface, text="MALE",padx = 20, variable=gender,value=1,font='cambria').place(x=120,y=200)
Radiobutton(interface, text="FEMALE",padx = 20, variable=gender, value=2,font='cambria').place(x=320,y=200)
Label(interface,text="MOBILE NO",font='cambria').place(x=120,y=250)
Entry(interface,textvar=number,font='cambria',bd=2).place(x=320,y=250)
Label(interface,text="MAIL ID",font='cambria').place(x=120,y=300)
Entry(interface,textvar=mail,font='cambria',bd=2).place(x=320,y=300)
Label(interface,text="PASSWORD",font='cambria').place(x=120,y=350)
Entry(interface,textvar=password1,font='cambria',bd=2,show="*").place(x=320,y=350)
Label(interface,text="CONFIRM PASSWORD",font='cambria').place(x=120,y=400)
Entry(interface,textvar=password2,font='cambria',bd=2,show="*").place(x=320,y=400)
Button(interface,text="SUBMIT",command=submit).place(x=390,y=450)

interface.mainloop()
