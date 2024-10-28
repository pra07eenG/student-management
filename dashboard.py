from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install pillow
from studentdetails import StudentClass 
from coursedetails import CourseClass
from attendence import AttendenceClass
from results import ResultsClass
from report import ReportClass


class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Managment System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.config(bg="white")

        #===icons=====
        self.logo_dash=ImageTk.PhotoImage(file="images/logo.jpeg")

        #===title=====
        title=Label(self.root,text="Student Managment System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=60)
        #===Menu====
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1500,height=80)

        btn_student=Button(M_Frame,text="Student Details",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_student).place(x=20,y=5,width=200,height=40)
        btn_course=Button(M_Frame,text="Course details",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_course).place(x=260,y=5,width=200,height=40)
        btn_attendence=Button(M_Frame,text="Attendence",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_attendence).place(x=500,y=5,width=200,height=40)
        btn_add=Button(M_Frame,text="Add  Results",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_results).place(x=750,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View  Results ",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_report).place(x=1000,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.exit).place(x=1250,y=5,width=200,height=40)

         #===content_window====
        self.courses_img=Image.open("images/courses.jpg")
        self.courses_img=self.courses_img.resize((920,350),Image.ANTIALIAS)
        self.courses_img=ImageTk.PhotoImage(self.courses_img)

        self.lbl_courses=Label(self.root,image=self.courses_img).place(x=300,y=180,width=920,height=350)

        #===footer=====
        footer=Label(self.root,text="SMS-Student Managment System\nContact Us for any Technical Issues: 9702378654",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

    #adding pages to buttons    
    def add_student(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_window)    

    def add_course(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_window)  

    def add_attendence(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=AttendenceClass(self.new_window)  

    def add_results(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=ResultsClass(self.new_window)  

    def add_report(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_window)  


    def exit(self):         
        op=messagebox.askyesno("confirm", "Do you really want to exit?", parent=self.root)         
        if op==True:            
            self.root.destroy()            
            #os.system("python login.py") 

    
        


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()        