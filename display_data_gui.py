from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import ttk
import mysql.connector

def disp():
  y=Tk()
  y.geometry("1600x500")
  l1=Label(y,text="Customer Data",font="Times 18 bold",pady=30).grid(row=0,column=1)
  # l1.pack(pady=40)
  b1=Button(y,text="Exit",width=10,bg='blue',fg='white',command=exit).grid(row=2,column=1)
  # b1.pack(side=BOTTOM,pady=50)
  mydb = mysql.connector.connect(
    host="localhost",
    user="test",                                #change user to your mysql user name
    password="test@123",                        #change password to your mysql password
    database="hotel_bill",
    auth_plugin='mysql_native_password'
  )

  mycursor = mydb.cursor()

  mycursor = mydb.cursor()
  if mydb.is_connected():
      print('Connected to MySQL database')
      mycursor.execute(""" SELECT * FROM customer_details """)
      records = mycursor.fetchall()
      total = mycursor.rowcount

  myframe=Frame(y)
  myframe.grid(row=1,column=1,pady=30)
  tview=ttk.Treeview(myframe,columns=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="10")
  tview.grid()

  tview.heading(1,text="Serial No")
  tview.column(1,minwidth=0,width=50)
  tview.heading(2,text="Room No")
  tview.column(2,minwidth=0,width=60)
  tview.heading(3,text="Name")
  tview.heading(4,text="Address")
  tview.heading(5,text="Phone No")
  tview.heading(6,text="Checkin Date")
  tview.heading(7,text="Checkout Date")
  tview.heading(8,text="Food Cost")
  tview.column(8,minwidth=0,width=100)
  tview.heading(9,text="Room Cost")
  tview.column(9,minwidth=0,width=100)
  tview.heading(10,text="GST")
  tview.column(10,minwidth=0,width=100)
  tview.heading(11,text="Total Cost")
  tview.column(11,minwidth=0,width=100)

  for i in records:
      tview.insert('','end',values=i)

  y.resizable(False,False)
