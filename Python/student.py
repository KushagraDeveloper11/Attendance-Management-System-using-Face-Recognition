from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1270x636+0+0")
        # self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #==============================================
        self.var_dep= StringVar()
        self.var_course= StringVar()
        self.var_year= StringVar()
        self.var_sem= StringVar()
        self.var_std_id= StringVar()
        self.var_std_name= StringVar()
        self.var_div= StringVar()
        self.var_roll= StringVar()
        self.var_gender= StringVar()
        self.var_dob= StringVar()
        self.var_email= StringVar()
        self.var_phone= StringVar()
        self.var_address= StringVar()
        self.var_teacher= StringVar()
        # self.var_dep= StringVar()
        
        
        #Logo
        img= Image.open(r"Python\Images\logo-9.png")
        img= img.resize((425,100), Image.LANCZOS)
        self.photoimg= ImageTk.PhotoImage(img)
      
        f_label= Label(self.root, image= self.photoimg)
        f_label.place(x=0, y=0, width=425, height= 100)
        
        #Image 1
        img1= Image.open(r"Python\Images\logo-9.png")
        img1= img1.resize((425,100), Image.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)
      
        f_label= Label(self.root, image= self.photoimg1)
        f_label.place(x=425, y=0, width=425, height= 100)
        
        #Image 2
        img2= Image.open(r"Python\Images\logo-9.png")
        img2= img2.resize((425,100), Image.LANCZOS)
        self.photoimg2= ImageTk.PhotoImage(img2)
      
        f_label= Label(self.root, image= self.photoimg2)
        f_label.place(x=850, y=0, width=425, height= 100)
        
         #Bg Image
        img3= Image.open(r"Python\Images\logo-9.png")
        img3= img3.resize((1270,600), Image.LANCZOS)
        self.photoimg3= ImageTk.PhotoImage(img3)
      
        bg_img= Label(self.root, image= self.photoimg3)
        bg_img.place(x=0, y=100, width=1270, height= 600)
        
        title_lbl= Label(bg_img, text="STUDENT DETAILS", font=("times new roman", 35, "bold"), bg="black", fg= "green")
        title_lbl.place(x=0, y=0, width=1270, height= 50)
        
        main_frame= Frame(bg_img, bd=2)
        main_frame.place(x=0, y=50, width= 1270, height= 600)
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=600)

        img_left= Image.open(r"Python\Images\logo-9.png")
        img_left= img_left.resize((720,130), Image.LANCZOS)
        self.photoimg_left= ImageTk.PhotoImage(img_left)
      
        f_label= Label(Left_frame, image= self.photoimg_left)
        f_label.place(x=5, y=0, width=720, height= 130)


        # current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=115)

        # department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman",12,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer Science","Civil","Mechanical","IT","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","FE","SE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        

        # Year
        year_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        # Semester
        sem_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only",width=20)
        sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        # class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        # student ID
        studentID_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        class_div_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone No.
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher's Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio Buttons
        radionbt1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="Yes")
        radionbt1.grid(row=6,column=0)

        radionbt2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="Yes")
        radionbt2.grid(row=6,column=1)

        # button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="White")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="White")
        btn_frame.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=580,height=600)


        img_right= Image.open(r"Python\Images\logo-9.png")
        img_right= img_right.resize((720,130), Image.LANCZOS)
        self.photoimg_left= ImageTk.PhotoImage(img_right)
      
        f_label= Label(Right_frame, image= self.photoimg_left)
        f_label.place(x=5, y=0, width=720, height= 130)


        # ============= Search System===============

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=700,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="Red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="read only",width=20)
        search_combo["values"]=("Select","Roll No","Phone NO")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        # ================table frame=================

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Dep","Course","Year","Sem","Id","Name","Div","Roll","Gender","DOB","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yviewview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Sem")
        self.student_table.heading("Id",text="Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Div")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        #=====================================================================================
        
    def add_data(self):
        pass
        
        
if __name__=="__main__":
    root= Tk()
    obj= Student(root)
    root.mainloop()