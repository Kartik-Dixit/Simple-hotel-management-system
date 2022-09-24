from tkinter import*
from tkinter import font
from resturant import *
from roominfo import *
import mysql.connector
from tkinter import messagebox

#



mydb = mysql.connector.connect(
  host="localhost",
  user="root",                                      #change user to your mysql user name
  password="system",                                #change password to your mysql password
  database="hotel_bill",
  auth_plugin='mysql_native_password'
)

# create database
mycursor= mydb.cursor()
# mycursor.execute("CREATE DATABASE hotel_bill")
#mycursor.execute("CREATE TABLE customer_details (id INT AUTO_INCREMENT PRIMARY KEY,roomno INT(3), name VARCHAR(255), address VARCHAR(255), phoneno VARCHAR(12), date_in VARCHAR(10) , date_out VARCHAR (10),food_cost INT(5), room_cost INT(6), gst float(8), total_cost float (8)) ;")

#mycursor = mydb.cursor()

def pinfo():
    m=Tk()
    def input():
        global room
        room=roomvalue.get()
        global name
        name=namevalue.get()
        global address
        address=addressvalue.get()
        global phone
        phone=phonevalue.get()
        global datein
        datein=dateinvalue.get()
        global dateout
        dateout=dateoutvalue.get()
        print(room,name,address,phone,datein,dateout)
        m.destroy()
        roomgui()
        

    m.geometry("555x555")
    Label(m,text="Customer Details",padx=100,pady=20,font="Times 13 bold").grid(row=0,column=3)
    Label(m,text="Room no",padx=2,pady=20).grid(row=1,column=2)
    Label(m,text="Name",padx=2,pady=20).grid(row=2,column=2)
    Label(m,text="Address",padx=2,pady=20).grid(row=3,column=2)
    Label(m,text="Phone number:",padx=2,pady=20).grid(row=4,column=2)
    Label(m,text="Check In Date",padx=2,pady=20).grid(row=5,column=2)
    Label(m,text="Check Out Date",padx=2,pady=20).grid(row=6,column=2)
    roomvalue=IntVar()
    namevalue=StringVar()
    addressvalue=StringVar()
    phonevalue=IntVar()
    dateinvalue=StringVar()
    dateoutvalue=StringVar()

    roomentery= Entry(m,textvariable=roomvalue)
    nameentery= Entry(m,textvariable=namevalue)
    addressentery= Entry(m,textvariable=addressvalue)
    phoneentery= Entry(m,textvariable=phonevalue)
    dateinentery= Entry(m,textvariable=dateinvalue)
    dateoutentery= Entry(m,textvariable=dateoutvalue)

    roomentery.grid(row=1,column=3)
    nameentery.grid(row=2,column=3)
    addressentery.grid(row=3,column=3)
    phoneentery.grid(row=4,column=3)
    dateinentery.grid(row=5,column=3)
    dateoutentery.grid(row=6,column=3)

    Button(text="Save and Next",command=input).grid(row=10,column=3)


    #.....................................................Room GUI..................................................


    def roomgui():
        n=Tk()
        obj=roomdetails()

        n.geometry("650x555")
        Label(n,text="Room Details",padx=100,pady=20,font="Times 13 bold").grid(row=0,column=2)

        def roomdata():
            room=check.get()
            acroom=AC.get()
            num=nights.get()
            global r_rent
            r_rent=obj.roomrent(room,acroom,num)
            n.destroy()
            foodgui()
                
        check=IntVar()
        AC=StringVar()
        nights=IntVar()
        Label(n,text="Please select a room").grid(row=1,column=1)

        room1= Radiobutton(n,text="Super Premium Room",variable=check,value=1).grid(row=2,column=1)
        room2= Radiobutton(n,text="Super Deluxe Room",variable=check,value=2).grid(row=2,column=2)
        room3= Radiobutton(n,text="Deluxe Room",variable=check,value=3).grid(row=3,column=1)
        room4= Radiobutton(n,text="Dormitory",variable=check,value=4).grid(row=3,column=2)

        Label(n,text="Do you need AC?").grid(row=5,column=1)

        Acroom1= Radiobutton(n,text="Yes",variable=AC,value="yes").grid(row=5,column=2)
        Acroom2= Radiobutton(n,text="NO",variable=AC,value="no").grid(row=5,column=3)

        Label(n,text="For how many night did you stay??").grid(row=7,column=1)
        Entry(n,textvariable=nights).grid(row=7,column=3)

        Button(n,text="Save and Next",command=roomdata).grid(row=10,column=2,pady=10)


        #...............................................Food GUI..................................................


    def foodgui():
        fobj=fooddetails()

        def food():
            bfood=breakfast.get()
            lfood=lunch.get()
            dfood=dinner.get()
            dd=day.get()
            global foodcost
            foodcost=fobj.calculate(bfood,lfood,dfood,dd)
            o.destroy()
            insert()

        o=Tk()
        o.geometry("555x555")
        breakfast=IntVar()
        lunch=IntVar()
        dinner=IntVar()
        day=IntVar()
        Label(o,text="Food purchased Details",padx=10,pady=20,font="Times 13 bold").grid(row=0,column=3)
        Label(o,text="Food Costs are as follows:",font="Times 10 bold").grid(row=1,column=2)
        Label(o,text="Breakfast ---> 150").grid(row=2,column=2)
        Label(o,text="Lunch ---> 500").grid(row=3,column=2)
        Label(o,text="Dinner ---> 300").grid(row=4,column=2)
        Label(o,text="Please select your food:").grid(row=5,column=2)
        c1=Checkbutton(o,text="Breakfast",variable=breakfast).grid(row=6,column=2)
        c2=Checkbutton(o,text="Lunch",variable=lunch,).grid(row=7,column=2)
        c3=Checkbutton(o,text="Dinner",variable=dinner).grid(row=8,column=2)
        Label(o,text="For how many days?").grid(row=9,column=2)
        Entry(o,textvariable=day).grid(row=9,column=3)
        Button(o,text="Save and Next",command=food).grid(row=10,column=3)

def insert():
    gst=0.12*(r_rent+foodcost)
    totalcost=r_rent+foodcost+gst
    # print(room, name, address, phone, datein, dateout, foodcost, r_rent, gst, totalcost)
    sql = "INSERT INTO customer_details (roomno, name, address, phoneno, date_in, date_out, food_cost, room_cost, gst, total_cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (room, name, address, phone, datein, dateout, foodcost, r_rent, gst, totalcost)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.\n")
