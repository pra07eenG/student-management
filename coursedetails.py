from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox 
import sqlite3

class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Managment System")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg="white") 

        # ===============title===============         
        title = Label(self.root, text="Subject Details", font=("goudy old style", 18,"bold"), bg="#033054",fg="white").place(x=10, y=15, width=1230, height=35)

        #============variables=========
        self.var_cid = StringVar()         
        self.var_course = StringVar()         
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_department = StringVar()
        self.var_subject = StringVar()
        self.var_subject_code = StringVar()

        #widgets
        lbl_course = Label(self.root, text="Course", font=("times new roman", 15), bg="white").place(x=10, y=70) 
        lbl_year = Label(self.root, text="Year", font=("times new roman", 15), bg="white").place(x=10, y=110)
        lbl_semester = Label(self.root, text="Semester", font=("times new roman", 15), bg="white").place(x=10, y=150) 
        lbl_department = Label(self.root, text="Department", font=("times new roman", 15), bg="white").place(x=10, y=190)
        lbl_subject = Label(self.root, text="Subject", font=("times new roman", 15), bg="white").place(x=10, y=230)
        lbl_subject_code = Label(self.root, text="Subject Code", font=("times new roman", 15), bg="white").place(x=10, y=270)
        
        #Entry
        #combobox for course, year, semester, department
        self.cmb_course=ttk.Combobox(self.root,textvariable=self.var_course, font=("times and romen", 15), state="readonly", justify=CENTER)
        self.cmb_course["values"]=("M.Tech","Degree","B.Tech","MBA","BBA")
        self.cmb_course.place(x=200,y=70,width=200)
        self.cmb_course.set("select course")

        self.cmb_year=ttk.Combobox(self.root,textvariable=self.var_year, font=("times and romen", 15), state="readonly", justify=CENTER)
        self.cmb_year["values"]=("1st","2nd","3rd","4th")
        self.cmb_year.place(x=200,y=110,width=200)
        self.cmb_year.set("select year")

        self.cmb_semester=ttk.Combobox(self.root,textvariable=self.var_semester, font=("times and romen", 15), state="readonly", justify=CENTER)
        self.cmb_semester["values"]=("1st","2nd","3rd","4th","5th","6th","7th","8th")
        self.cmb_semester.place(x=200,y=150,width=200)
        self.cmb_semester.set("select semester")

        self.cmb_department=ttk.Combobox(self.root,textvariable=self.var_department, font=("times and romen", 15), state="readonly", justify=CENTER)
        self.cmb_department["values"]=("CSE","IT","ECE","EEE","CIVIL","Mech")
        self.cmb_department.place(x=200,y=190,width=200)
        self.cmb_department.set("select department")

        self.txt_subject=Entry(self.root,textvariable=self.var_subject, font=("times and romen", 15), bg="lightyellow").place(x=200,y=230,width=200,height=35)
        self.txt_subject_code=Entry(self.root,textvariable=self.var_subject_code, font=("times and romen", 15), bg="lightyellow").place(x=200,y=270,width=200,height=35)
        
        
        #buttons for save, update, delete, clear
        self.btn_add = Button(self.root, text="Add", font=("times and romen", 15), bg="blue", fg="white",command=self.add_course).place(x=10,y=330, width=100, height=35)               
        self.btn_update = Button(self.root, text="Update", font=("times and romen", 15), bg="blue",fg="white",command=self.update_course).place(x=120,y=330, width=100, height=35)         
        self.btn_delete = Button(self.root, text="Delete", font=("times and romen", 15), bg="blue",fg="white",command=self.delete_course).place(x=230,y=330, width=100, height=35)          
        self.btn_clear = Button(self.root, text="Clear", font=("times and romen", 15), bg="blue", fg="white",command=self.clear_course).place(x=340,y=330, width=100, height=35)
        
        
        #search panel  
        lbl_search= Label(self.root, text="Search By", font=("times new roman", 15),bg="white",fg="black").place(x=450, y=70)         
        self.var_search = StringVar() 
        self.var_searchentry=StringVar()         
        self.cmb_search=ttk.Combobox(self.root,font=("times new roman",15),state="readonly",textvariable=self.var_search,justify=CENTER)
        self.cmb_search["values"]=("Course","Department")
        self.cmb_search.place(x=550,y=70,width=200)
        self.cmb_search.set("select")        
        txt_search= Entry(self.root, font=("times new roman", 15),bg="lightgray",fg="black",textvariable=self.var_searchentry).place(x=760, y=70, width=200,height=35)         
        btn_search = Button(self.root, text="Search", font=("times new roman", 15), bg="blue", fg="white",command=self.search_course).place(x=970, y=70, width=100, height=35)

        #content
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)         
        self.C_Frame.place(x=450, y=110, width=700, height=400) 

        #scroll bar
        scroll_y = Scrollbar(self.C_Frame, orient=VERTICAL)         
        scroll_x = Scrollbar(self.C_Frame, orient=HORIZONTAL)         
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "course","year", "semester", "department", "subject","subject_code"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)         
        scroll_y.pack(side=RIGHT, fill=Y)         
        scroll_x.config(command=self.CourseTable.xview)         
        scroll_y.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="CID")         
        self.CourseTable.heading("course", text="Course")         
        self.CourseTable.heading("year", text="Year")         
        self.CourseTable.heading("semester", text="Semester")         
        self.CourseTable.heading("department", text="Department")
        self.CourseTable.heading("subject", text="Subject")
        self.CourseTable.heading("subject_code", text="Subject Code")        
        self.CourseTable["show"] = "headings"        
        self.CourseTable.column("cid", width=100)         
        self.CourseTable.column("course", width=100)         
        self.CourseTable.column("year", width=100)         
        self.CourseTable.column("semester", width=100)         
        self.CourseTable.column("department", width=100)
        self.CourseTable.column("subject", width=100)
        self.CourseTable.column("subject_code", width=100)     
        self.CourseTable.pack(fill=BOTH, expand=1)         
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)         
        self.show()


    #adding course data to table
    def add_course(self):
        conn=sqlite3.connect(database="srms.db")
        cur=conn.cursor()
        try:
            if self.var_course.get() not in ("M.Tech","Degree","B.Tech","MBA","BBA") or self.var_subject.get()=="":
                messagebox.showerror("Error", "Course name and subject is required", parent=self.root)
            else:                 
                cur.execute("INSERT INTO courses (course, year, semester, department, subject, subject_code) values(?,?,?,?,?,?)",(
                    self.var_course.get(),        
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_department.get(),
                    self.var_subject.get(),
                    self.var_subject_code.get()
                ))   
                conn.commit()
                messagebox.showinfo("Success","Course added successfully", parent=self.root)
                self.show()

        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)    

    def show(self):
        conn=sqlite3.connect(database="srms.db")
        cur=conn.cursor()
        try:
                cur.execute("select * FROM courses")
                rows=cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert("",END,values=row)
        except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)

    def get_data(self,ev):     
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_course.set(row[1])        
        self.var_year.set(row[2])
        self.var_semester.set(row[3])
        self.var_department.set(row[4])
        self.var_subject.set(row[5])
        self.var_subject_code.set(row[6])

    def update_course(self):
        conn=sqlite3.connect(database="srms.db")
        cur=conn.cursor()
        try:
            if self.var_course.get() not in ("M.Tech","Degree","B.Tech","MBA","BBA"):
                messagebox.showerror("Error", "select course from the list to update", parent=self.root)
            else:
                r=self.CourseTable.focus()
                content=self.CourseTable.item(r)
                row=content["values"]   
                cid = row[0]
                cur.execute("UPDATE courses SET course=?, year=?, semester=?, department=?, subject=?, subject_code=? WHERE cid=?",(
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_department.get(),
                    self.var_subject.get(),
                    self.var_subject_code.get(),
                    cid
                ))    
                conn.commit()
                messagebox.showinfo("Success","Course updated successfully", parent=self.root)
                self.show()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)   

    def clear_course(self):
            self.show()
            self.var_course.set("select course")      
            self.var_year.set("select year")        
            self.var_semester.set("select semester")
            self.var_department.set("select department")
            self.var_subject.set("")
            self.var_subject_code.set("")
            self.var_search.set("Select")
            self.var_searchentry.set("") 

    def delete_course(self):
        conn=sqlite3.connect(database="srms.db")
        cur=conn.cursor()
        try:
            r=self.CourseTable.focus()
            content=self.CourseTable.item(r)
            row=content["values"]   
            cid = row[0]       
            print(cid)
            cur.execute("select * FROM courses  WHERE cid=?", (cid,))                 
            row=cur.fetchone()                 
            if row== None:                     
                messagebox.showerror("Error", "Please select course from the list to delete", parent=self.root)                 
            else: 
                ask=messagebox.askyesno("Delete","Do you want to delete this course?",parent=self.root)
                if ask == True:
                    cur.execute("DELETE FROM courses where cid=?", (cid,))
                    conn.commit()
                    messagebox.showinfo("Success","Course deleted successfully",parent=self.root)
                    self.clear_course()
        except Exception as es:
                messagebox.showerror("Error","Please select course from the list to delete",parent=self.root)

    def search_course(self):
        conn=sqlite3.connect(database="srms.db")
        cur=conn.cursor()
        try:
            if self.var_searchentry.get() not in ("Course","Department") or self.var_searchentry.get()=="":
                messagebox.showerror("Error", "select search criteria from the list", parent=self.root)
            else:
                cur.execute(f"SELECT * FROM courses WHERE {self.var_search.get()} LIKE '%{self.var_searchentry.get()}%'")
                rows=cur.fetchall() 
                if len(rows)!=0:
                    self.CourseTable.delete(*self.CourseTable.get_children())
                    for row in rows:
                        self.CourseTable.insert("", END, values=rows)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)       
        

if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()                   