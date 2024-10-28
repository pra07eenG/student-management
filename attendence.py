from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox 
import tkinter as tk
import sqlite3

class AttendenceClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Managment System")
        self.root.geometry("1250x700+100+50")
        self.root.config(bg="white") 

        # ===============title===============         
        title = Label(self.root, text="Attendence Details", font=("goudy old style", 30, "bold"), bg="#033054",fg="white").place(x=10, y=15, width=1230, height=40)

        # ==========Variables==============         
        self.var_course = StringVar()         
        self.var_year = StringVar()         
        self.var_department = StringVar()
        self.var_login_name = StringVar()
        self.var_login_password = StringVar()

        #widgets
        lbl_course = Label(self.root, text="Course", font=("times new roman", 15), bg="white").place(x=60, y=70) 
        lbl_year = Label(self.root, text="Year", font=("times new roman", 15), bg="white").place(x=450, y=70)
        lbl_department = Label(self.root, text="Department", font=("times new roman", 15), bg="white").place(x=850, y=70)
        lbl_login_name = Label(self.root, text="Login Name", font=("times new roman", 15), bg="white").place(x=220, y=130)
        lbl_login_password = Label(self.root, text="Login Password", font=("times new roman", 15), bg="white").place(x=780, y=130)

        #combobox
        self.cmb_course=ttk.Combobox(self.root,textvariable=self.var_course, font=("times and romen", 15), state="readonly", justify=CENTER)
        self.cmb_course["values"]=("M.Tech","Degree","B.Tech","MBA","BBA")
        self.cmb_course.place(x=150,y=70,width=200,height=30)
        self.cmb_course.set("select course")

        self.cmb_year=ttk.Combobox(self.root,textvariable=self.var_year, font=("times and romen", 15), state="readonly", justify=CENTER)
        self.cmb_year["values"]=("1st","2nd","3rd","4th")
        self.cmb_year.place(x=550,y=70,width=200,height=30)
        self.cmb_year.set("select year")

        self.cmb_department=ttk.Combobox(self.root,textvariable=self.var_department, font=("times and romen", 15), state="readonly", justify=CENTER)
        self.cmb_department["values"]=("CSE","IT","ECE","EEE","CIVIL","Mech")
        self.cmb_department.place(x=1000,y=70,width=200,height=30)
        self.cmb_department.set("select department")

        #entry fields
        self.txt_login_name=Entry(self.root,textvariable=self.var_login_name, font=("times and romen", 15), bg="lightyellow").place(x=330,y=130,width=200,height=30)
        self.txt_login_password=Entry(self.root,textvariable=self.var_login_password, font=("times and romen", 15), bg="lightyellow").place(x=920,y=130,width=200,height=30)

        btn_login = Button(self.root, text="Login", font=("times and romen", 15), bg="#eb5377", fg="white",cursor="hand2",command=self.login).place(x=550,y=187, width=200, height=35)  


    def login(self):
        if self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_department.get()=="Select Department" or self.var_login_name.get()=="" or self.var_login_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            username=self.var_login_name.get()
            password=self.var_login_password.get()
            conn=sqlite3.connect(database="srms.db")
            cur=conn.cursor()
            cur.execute("SELECT password FROM login where username=?",(username,))
            row=cur.fetchone()                 
            if row== None:                     
                messagebox.showerror("Error", "User does not have access to attendence page", parent=self.root)                 
            else: 
                if row[0]==password:
                    messagebox.showinfo("Success","Login Successfull",parent=self.root)
                    red_buttons=[]
                    absentees_list=[]
                    def toggle_color(button):
                        current_color=button.cget("bg")
                        new_color="green" if current_color =="red" else "red"
                        button.config(bg=new_color)
                        if new_color=="green":
                            red_buttons.remove(button)
                        elif new_color=="red":
                            red_buttons.append(button)

                    def submit():
                        if len (red_buttons)==0:
                            messagebox.showerror("Error","Please select attendence",parent=self.root)
                        else:
                            for button in red_buttons:
                                rollno =button.cget("text")
                                absentees_list.append(rollno)
                            print(absentees_list)
                            ask=messagebox.askyesno("Confirm","Do you want to submit attendence?")
                            if ask==True:
                                cur.execute("INSERT INTO attendence (course,year,department,absentees) VALUES (?,?,?,?)",(
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_department.get(),
                                    str(absentees_list)
                                ))     
                                conn.commit()
                                messagebox.showinfo("Absentees","Absentees are : "+str(absentees_list),parent=self.root)
                        self.root.destroy()
                    self.rollno_frame=Frame(self.root,bd=2,relief=RIDGE)
                    self.rollno_frame.place(x=400,y=250,width=500,height=320)

                    count=0
                    rollno=1
                    for i in range(0,6):
                        for j in range(0,10):
                            button=Button(self.rollno_frame,text=str(rollno),font=("times new roman",15),bg="red")
                            count+=1
                            rollno+=1
                            button.config(command=lambda b=button: toggle_color(b))
                            button.grid(row=i,column=j,padx=5,pady=5)
                            red_buttons.append(button)

                    submit_button=Button(self.root,text="submit",font=("times new roman",15),bg="#eb5377",fg="white",cursor="hand2",command=submit).place(x=550,y=600,width=200,height=35)

                else:
                    messagebox.showerror("Error","Invalid Password",parent=self.root)



                       
        
        


if __name__=="__main__":
    root=Tk()
    obj=AttendenceClass(root)
    root.mainloop()                           