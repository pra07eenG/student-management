from tkinter import *
from tkinter import ttk,messagebox
import sqlite3  

class ReportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #=====variables
        self.var_subject=StringVar()
        
        # =====================title============================
        title=Label(self.root,text="View Student Results",font=("goudy old style",18,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=50)
        #==========================search=========================
        self.var_search=StringVar()
        self.var_id=""
        lbl_search=Label(self.root,text="Select By Roll No",font=("goudy old style",15,'bold'),bg='white').place(x=280,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg='lightgreen').place(x=500,y=100,width=150)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,'bold'),bg="#03a9f4",fg='white',cursor="hand2",command=self.search).place(x=680,y=100,width=100,height=36)
        btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,'bold'),bg="orange",fg='white',cursor="hand2",command=self.clear).place(x=800,y=100,width=100,height=36)
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_subject=Label(self.root,text="Subject",font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks=Label(self.root,text="Marks obtained",font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        self.roll=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.subject=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.subject.place(x=450,y=280,width=150,height=50)
        self.marks=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150,height=50)
        self.full=Label(self.root, font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.full.place(x=750,y=280,width=150,height=50)
        self.per=Label(self.root, font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)

        #=======================button delete======================
        btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,'bold'),bg="red",fg='white',cursor="hand2",command=self.delete).place(x=500,y=350,width=150,height=36)
        #============================================================

    def search(self):
        conn=sqlite3.connect(database="srms.db")
        cur=conn.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("select * from results where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.subject.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                else: 
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_id="" 
        self.roll.config(text="")
        self.name.config(text="")
        self.subject.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    def delete(self):
        conn=sqlite3.connect(database="srms.db")
        cur=conn.cursor()
        try:
            if self.var_subject.get() == "":
                messagebox.showerror("Error","search Student Result first",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        conn.commit()
                        messagebox.showinfo("Delete","Result deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__=="__main__":
    root=Tk()
    obj=ReportClass(root)
    root.mainloop()
