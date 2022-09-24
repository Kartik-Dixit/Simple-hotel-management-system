from tkinter import *
from tkinter import messagebox
from input_data_gui import *
from display_data_gui import *

z=Tk()
passwd=StringVar()
def validate():
    password=passwd.get()
    if password=="INT213":          #Change password to your wish
        z.destroy()
        run()
    else:
        messagebox.showerror("showerror","Password Incorrect!!!")

z.geometry("450x150")
Label(z,text="Simple Hotel Management System",padx=0,pady=20,font="Times 13 bold").grid(row=0,column=2)
Label(z,text="Enter Password:").grid(row=1,column=1)
pssentry=Entry(z,textvariable=passwd).grid(row=1,column=2)
Button(z,text="Enter",command=validate).grid(row=3,column=2)

def run():
    k=Tk()
    def move():
        dat=data.get()
        if dat==1:
            k.destroy()
            pinfo()
        else:
            k.destroy()
            disp()

    k.geometry("555x555")
    data=IntVar()
    r1= Radiobutton(k,text="Input Customer data",variable=data,value=1).grid(row=1,column=2)
    r2= Radiobutton(k,text="Display database",variable=data,value=2).grid(row=2,column=2)
    Button(k,text="Continue->",command=move).grid(row=4,column=3)

z.mainloop()
