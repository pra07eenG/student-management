from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox 
import sqlite3

class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Managment System")
        self.root.geometry("1250x700+100+50")
        self.root.config(bg="white") 

        # ===============title===============         
        title = Label(self.root, text="Student Details", font=("goudy old style", 18, "bold"), bg="#033054",fg="white").place(x=10, y=15, width=1230, height=35)

        # ==========Variables==============         
        self.Roll_No_var = StringVar()         
        self.Name_var = StringVar()         
        self.Course_var = StringVar()
        self.Department_var = StringVar()
        self.Year_var = StringVar()
        self.Semester_var = StringVar()
        self.DOB_var = StringVar()
        self.Email_var = StringVar()
        self.Parent_No_var = StringVar()
        self.Address_var = StringVar()

        # ==============Widgets=================         
        lbl_roll = Label(self.root, text="Roll No", font=("times new roman", 15), bg="white",fg="black").place(x=10, y=70) 
        self.txt_roll = Entry(self.root, textvariable=self.Roll_No_var,font=("times new roman", 15),bg="lightgray",fg="black")
        self.txt_roll.place(x=150, y=70, width=200,height=35)
        lbl_name = Label(self.root, text="Name", font=("times new roman", 15), bg="white", fg="black").place(x=10,y=120) 
        txt_Name = Entry(self.root, textvariable=self.Name_var, font=("times new roman", 15),bg="lightgray",fg="black").place(x=150, y=120, width=200,height=35)
        lbl_course=Label(self.root,text="Course", font=("times new roman", 15), bg="white", fg="black").place(x=10,y=170)
        self.txt_course=ttk.Combobox(self.root, font=("times new roman", 15), state="readonly", textvariable=self.Course_var, values=("B.Tech", "M.Tech","BBA","MBA","Degree")).place(x=150, y=170, width=200,height=35)
        self.Course_var.set("Select Course")
        lbl_department=Label(self.root,text="Department", font= ("times new roman", 15), bg="white", fg="black").place(x=10,y=220)
        self.txt_department=ttk.Combobox(self.root, font= ("times new roman", 15), state="readonly", textvariable=self.Department_var, values=("CSE", "ECE","IT","EEE","Mech","Civil")).place(x=150, y=220, width=200,height=35)
        self.Department_var.set("Select Department")
        lbl_year=Label(self.root, text="Year", font= ("times new roman", 15), bg="white", fg="black").place(x=10,y=270)
        self.txt_year=ttk.Combobox(self.root, font=("times new roman", 15), state="readonly", textvariable=self.Year_var,values=("1st", "2nd", "3rd", "4th")).place(x=150, y=270, width=200,height=35)
        self.Year_var.set("Select Year")
        lbl_semester=Label(self.root, text="Semester", font= ("times new roman", 15), bg="white", fg="black").place(x=10,y=320)
        self.txt_semester=ttk.Combobox(self.root, font =("times new roman", 15), state="readonly", textvariable=self.Semester_var, values=("1st", "2nd", "згd","4th","5th","6th","7th","8th")).place(x=150, y=320, width=200,height=35)
        self.Semester_var.set("Select Semester")
        lbl_dob=Label(self.root, text="DOB", font=("times new roman", 15), bg="white", fg="black").place(x=10,y=370)
        txt_dob=Entry(self.root, font=("times new roman", 15), bg="lightgray", fg="black", textvariable=self.DOB_var).place(x=150,y=370,width=200,height=35)
        lbl_email=Label(self.root,text="Email", font= ("times new roman", 15), bg="white", fg="black").place(x=10,y=420)
        txt_email=Entry(self.root, font=("times new roman", 15), bg="lightgray", fg="black", textvariable=self.Email_var).place(x=150,y=420, width=200, height=35)
        lbl_parents_no=Label(self.root, text="Parents No", font= ("times new roman", 15), bg="white", fg="black").place(x=10,y=470)
        txt_parents_no=Entry(self.root, font =("times new roman", 15), bg="lightgray", fg="black",textvariable=self.Parent_No_var).place(x=150,y=470, width=200, height=35)
        lbl_address=Label(self.root,text="Address", font =("times new roman", 15), bg="white", fg="black").place(x=10,y=520)
        self.txt_address=Text(self.root, font=("times new roman", 15), bg="lightgray", fg="black")
        self.txt_address.place(x=150,y=520, width=200,height=100)
       
        

        # ==============Buttons=============         
        self.btn_add = Button(self.root, text="Add", font=("times and romen", 15), bg="#033054", fg="white",command=self.add_students).place(x=10,y=640, width=100, height=35)               
        self.btn_update = Button(self.root, text="Update", font=("times and romen", 15), bg="#033054",fg="white",command=self.update_students).place(x=120,y=640, width=100, height=35)         
        self.btn_delete = Button(self.root, text="Delete", font=("times and romen", 15), bg="#033054",fg="white",command=self.delete_student).place(x=230,y=640, width=100, height=35)          
        self.btn_clear = Button(self.root, text="Clear", font=("times and romen", 15), bg="#033054", fg="white",command=self.clear_students).place(x=340,y=640, width=100, height=35) 

        # =============Search panel===============  
        lbl_search= Label(self.root, text="Search By", font=("times new roman", 15),bg="white",fg="black").place(x=370, y=70) 
        self.search_var = StringVar() 
        self.var_searchentry=StringVar()        
        self.combo_search=ttk.Combobox(self.root,font=("times new roman",15),state="read only",textvariable=self.search_var,values=("Roll No","Name","Department","Course")).place(x=470,y=70, width=200, height=35)
        self.search_var.set("select")        
        txt_search= Entry(self.root, font=("times new roman", 15),bg='lightgray',fg="black",textvariable=self.var_searchentry).place(x=680, y=70, width=200,height=35)         
        btn_search = Button(self.root, text='Search', font=("times new roman", 15), bg="blue", fg='white',cursor="hand2",command=self.search_students).place(x=900, y=70, width=200, height=35)

        #================content================         
        self.C_Frame = Frame(self.root, bd=4, relief=RIDGE,bg="white")         
        self.C_Frame.place(x=370, y=120, width=800, height=500) 

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)         
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)         
        self.student_table = ttk.Treeview(self.C_Frame, columns=("Roll", "Name","Course", "Department", "Year", "Semester","DOB","Email","Parents No","Address"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)         
        scrolly.pack(side=RIGHT, fill=Y)         
        scrollx.config(command=self.student_table.xview)         
        scrolly.config(command=self.student_table.yview)

        self.student_table.heading("Roll", text="Roll No")         
        self.student_table.heading("Name", text="Name")         
        self.student_table.heading("Course", text="Course")         
        self.student_table.heading("Department", text="Department")         
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Parents No", text="Parents No")
        self.student_table.heading("Address", text="Address")        
        self.student_table["show"] = "headings"        
        self.student_table.column("Roll", width=100)         
        self.student_table.column("Name", width=100)         
        self.student_table.column("Course", width=100)         
        self.student_table.column("Department", width=100)         
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Parents No", width=100)  
        self.student_table.column("Address", width=100)     
        self.student_table.pack(fill=BOTH, expand=1)         
        self.student_table.bind("<ButtonRelease-1>", self.get_data)         
        self.show_students()

    #adding buttons for save, update, delete, clear
    def add_students(self):
        conn=sqlite3.connect(database="srms.db")
        cur=conn.cursor()
        try:
            if self.Roll_No_var.get()=="":
                messagebox.showerror("Error", "Roll No is required", parent=self.root)
            else:                 
                cur.execute("select * from student  where roll_No=?", (self.Roll_No_var.get(),))                 
                row=cur.fetchone()                 
                if row!= None:                     
                    messagebox.showerror("Error", "Roll No already exists", parent=self.root)                 
                else: 
                    cur.execute("insert into student values (?,?, ?, ?, ?, ?, ?, ?,?,?)",(  
                                self.Roll_No_var.get(),      
                                self.Name_var.get(),         
                                self.Course_var.get (),
                                self.Department_var.get(),
                                self.Year_var.get(),
                                self.Semester_var.get(),
                                self.DOB_var.get (),
                                self.Email_var.get (),
                                self.Parent_No_var.get(),
                                self.txt_address.get(1.0,END)
                            ))
                    conn.commit()
                self.show_students()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
                #con.close()
        except Exception as e:
            messagebox.showerror("Error",f"error due to: {str(e)}")

    def show_students(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror("Error",f"Error due to: {str(e)}")

    def get_data(self,ev):
        self.txt_roll.config(state="readonly")
        self.txt_roll
        r=self.student_table.focus()
        content=self.student_table.item(r)
        row=content["values"]
        #print(row)
        self.Roll_No_var.set(row[0])      
        self.Name_var.set(row[1])        
        self.Course_var.set(row[2])
        self.Department_var.set(row[3])
        self.Year_var.set(row[4])
        self.Semester_var.set(row[5])
        self.DOB_var.set(row[6])
        self.Email_var.set(row[7])
        self.Parent_No_var.set(row[8]),
        self.txt_address.delete(1.0,END)
        self.txt_address.insert(END,row[9])
    
    def update_students(self):
        conn=sqlite3.connect(database="srms.db")
        cur=conn.cursor()
        try:
            if self.Roll_No_var.get()=="":
                messagebox.showerror("Error","Roll No is required",parent=self.root)
            else:
                cur.execute("select * from student where roll_no=?",(self.Roll_No_var.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student roll no from list",parent=self.root)
                else:
                    cur.execute("update student set name=?,course=?,department=?,year=?,semester=?,dob=?,email=?,parents_no=?,address=? where roll_no=?",
                                (
                                        self.Name_var.get(),
                                        self.Course_var.get(),
                                        self.Department_var.get(),
                                        self.Year_var.get(),
                                        self.Semester_var.get(),
                                        self.DOB_var.get(),
                                        self.Email_var.get(),
                                        self.Parent_No_var.get(),
                                        self.txt_address.get(1.0, END),
                                        self.Roll_No_var.get()
                                ))
                    conn.commit()
                    messagebox.showinfo("Success","Student details has been Updated Successfully",parent=self.root)
                    self.show_students()
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")

    def clear_students(self):
        self.show_students()
        self.Roll_No_var.set("")      
        self.Name_var.set("")        
        self.Course_var.set("Select Course")
        self.Department_var.set("Select Department")
        self.Year_var.set("Select Year")
        self.Semester_var.set("Select Semester")
        self.DOB_var.set("")
        self.Email_var.set("")
        self.Parent_No_var.set("")
        self.txt_address.delete(1.0,END)
        self.search_var.set("select")
        self.var_searchentry.set("")
        self.txt_roll.config(state="normal")       

    def delete_student(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.Roll_No_var.get()=="":
                messagebox.showerror("Error", "Roll No is required", parent=self.root)
            else:                 
                cur.execute("select * from student  where roll_no=?", (self.Roll_No_var.get(),))                 
                row=cur.fetchone()                 
                if row== None:                     
                    messagebox.showerror("Error", "select student roll no from list", parent=self.root)                 
                else: 
                    ask=messagebox.askyesno("confirm","Do you want to delete this student?",parent=self.root)
                    if ask == True:
                        cur.execute("delete from student where roll_no=?", (self.Roll_No_var.get(),))
                        con.commit()
                        messagebox.showinfo("success","Student details has been deleted successfully",parent=self.root)
                        self.clear_students()
        except Exception as e:
            messagebox.showerror("Error",f"Error due to: {str(e)}")       

    #sidepanel search button
    def search_students(self):
        conn=sqlite3.connect(database="srms.db")
        cur=conn.cursor()
        try:
            if self.var_searchentry.get()=="":
                messagebox.showerror("Error","Search input required",parent=self.root)
            else:
                type=self.search_var.get()
                if type=="Roll No":
                    cur.execute("select * from student where roll_no", (self.var_searchentry.get(),))
                    rows=cur.fetchall()
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('',END,values=row)
                elif type=="Name":
                    cur.execute(f"select * from student where name like '%{self.var_searchentry.get()}%'")
                    rows=cur.fetchall()
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('',END,values=row)   
                elif type=="Department":
                    cur.execute(f"select * from student where department like '%{self.var_searchentry.get()}%'")
                    rows=cur.fetchall()
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('',END,values=row)   
                elif type=="Course":
                    cur.execute(f"select * from student where course like '%{self.var_searchentry.get()}%'")
                    rows=cur.fetchall()
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('',END,values=row)                                                 
                else:
                    messagebox.showerror("Error","select search criteria",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}")
                

if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()                   