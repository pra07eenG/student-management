from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
import os
import tkinter as tk
from dashboard import RMS

class Login:
    def __init__(self, root):
       self.root=root
       self.root.title("Student Managment System")
       self.root.geometry("700x480+300+100")
       self.root.config(bg="light blue")
       
       #=========variables=============
       self.username = StringVar()
       self.password = StringVar()

       #==========title============
       title=Label(self.root,text="Login System",font=("goudy old style",30,"bold"),bg="#033054",fg="white").place(x=10,y=10,width=680,height=40)

       #===========frame==========
       Login_Frame=Frame(self.root,bg="white")
       Login_Frame.place(x=50,y=90,width=600,height=350)

       #==========title============
       title=Label(Login_Frame,text="Login Here",font=("ariel",30,"bold"),bg="white",fg="green").place(x=20,y=28)

       lbl_user=Label(Login_Frame,text="Username",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=20,y=98)
       txt_user=Entry(Login_Frame,textvariable=self.username,font=("times new roman",15),bg="lightgray").place(x=170,y=100,height=35,width=300)

       lbl_pass=Label(Login_Frame,text="Password",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=20,y=170)
       txt_pass=Entry(Login_Frame,textvariable=self.password,font=("times new roman",20),bg="lightgray").place(x=170,y=170,height=35,width=300)

       btn_login=Button(Login_Frame,text="Login",font=("times new roman",15,"bold"),bg="#B00857",fg="white",cursor="hand2",command=self.login).place(x=60,y=250,width=200,height=40)


    def login(self):
        if self.login == "" or self.password == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = sqlite3.connect("srms.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM signin WHERE username = ? AND password = ?", (self.username.get(), self.password.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                messagebox.showinfo("Success", "Welcome")
            conn.close()
        self.new_window = Toplevel(self.root)
        self.new_obj = RMS(self.new_window)
        self.root.withdraw()                  




if __name__=="__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()               