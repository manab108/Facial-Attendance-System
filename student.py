from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os  

class Student:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #=========================variables========================
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_sem=StringVar()
        self.var_year=StringVar()
        self.var_std_Id=StringVar()
        self.var_section=StringVar()
        self.var_DOB=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_subCode=StringVar()


    

        #f image
        img = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\facial_recognition_action.jpg")
        img = img.resize((500, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=150)


        #second image
        img1 = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\facialrecognition.png")
        img1 = img1.resize((500, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=150)


        # third image 
        img2 = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\eye.jpg")
        img2 = img2.resize((500, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=150)


       #bg image
        img3 = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\image1.jpeg")
        img3 = img3.resize((1500, 600), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1500, height=650)

        title_lbl = Label(bg_img, text="STUDENT MANAGMENT BLOCK", font=("times new roman", 35, "bold"), bg="light blue", fg="grey")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1450,height=555) 
        

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="skyblue",relief=RIDGE,text="Student Details",font=("times new roman",13,"bold"))
        Left_frame.place(x=10,y=10,width=700,height=530)

        img_left = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\image1.jpeg")
        img_left = img_left.resize((720, 100), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=80)
        
        #current course information
        Current_Course_frame=LabelFrame(main_frame,bd=2,bg="skyblue",relief=RIDGE,text="Current Course Information",font=("times new roman",13,"bold"))
        Current_Course_frame.place(x=12,y=110,width=697,height=110)
         

        #department 
        department_label=Label(Current_Course_frame,text="Department",font=("times new roman",13,"bold"),bg="skyblue")
        department_label.grid(row=0,column=0,padx=10,sticky=W)
        
        department_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="read only") 
        department_combo["values"]=("Select Department","CSE","ECE","EE","EIE","ME")
        department_combo.current(0)
        department_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_label=Label(Current_Course_frame,text="Course",font=("times new roman",13,"bold"),bg="skyblue")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="read only") 
        course_combo["values"]=("Select Course","BTech","MTech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(Current_Course_frame,text="Year",font=("times new roman",13,"bold"),bg="skyblue")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="read only") 
        year_combo["values"]=("Select Year","2020-2024","2021-2025","2022-2026","2023-2027")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

         #semester
        semester_label=Label(Current_Course_frame,text="Semester",font=("times new roman",13,"bold"),bg="skyblue")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_sem,font=("times new roman",13,"bold"),state="read only") 
        semester_combo["values"]=("Select Semester","1-sem","2-sem","3-sem","4-sem","5-sem","6-sem","7-sem","8-sem")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        Class_student_frame=LabelFrame(main_frame,bd=2,bg="skyblue",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Class_student_frame.place(x=12,y=225,width=697,height=313)


       #student ID
        studentId_label=Label(Class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="skyblue")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_Id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(Class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="skyblue")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(Class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        

        #class section
        class_div_label=Label(Class_student_frame,text="Class Section:",font=("times new roman",13,"bold"),bg="skyblue")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_div_entry=ttk.Entry(Class_student_frame,textvariable=self.var_section,width=20,font=("times new roman",13,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        section_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_section,font=("times new roman",13,"bold"),state="read only",width=18) 
        section_combo["values"]=("Select Section","A","B")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll NO
        roll_no_label=Label(Class_student_frame,text="Roll No. :",font=("times new roman",13,"bold"),bg="skyblue")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(Class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #Gender
        Gender_label=Label(Class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="skyblue")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="read only",width=18) 
        Gender_combo["values"]=("Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


         #DOB
        DOB_label=Label(Class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="skyblue")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Gender_entry=ttk.Entry(Class_student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",13,"bold"))
        Gender_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

         #Eamil
        email_label=Label(Class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="skyblue")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(Class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         #Phone no
        PhoneNo_label=Label(Class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="skyblue")
        PhoneNo_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        PhoneNo_entry=ttk.Entry(Class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        PhoneNo_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

         #Parmanent Adress
        adress_label=Label(Class_student_frame,text="Adress:",font=("times new roman",13,"bold"),bg="skyblue")
        adress_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        adress_entry=ttk.Entry(Class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        adress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

         #subject code
        subjectCode_label=Label(Class_student_frame,text="Subject Code:",font=("times new roman",13,"bold"),bg="skyblue")
        subjectCode_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        subjectCode_entry=ttk.Entry(Class_student_frame,textvariable=self.var_subCode,width=20,font=("times new roman",13,"bold"))
        subjectCode_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio Button
        #textvariable=self.var_radio1,
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        #textvariable=self.var_radio2,
        
        radiobtn2=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="skyblue")
        btn_frame.place(x=0,y=200,width=690,height=45)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey") 
        save_btn.grid(row=0,column=0,pady=5,padx=6)

        update_btn=Button(btn_frame,text="Update",width=15,command=self.update_data,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey")
        update_btn.grid(row=0,column=1,pady=5,padx=6)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey") 
        delete_btn.grid(row=0,column=2,pady=5,padx=6)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey") 
        reset_btn.grid(row=0,column=3,pady=5,padx=6)



        btn2_frame=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="skyblue")
        btn2_frame.place(x=0,y=247,width=690,height=43)

        take_photo_btn=Button(btn2_frame,text="Take Photo Sample",command=self.generate_dataset,width=32,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey") 
        take_photo_btn.grid(row=0,column=0,pady=2,padx=6)
         
        update_photo_btn=Button(btn2_frame,text="Update Photo Sample",width=32,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey") 
        update_photo_btn.grid(row=0,column=1,pady=2,padx=6) 


       


        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="skyblue",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=720,y=10,width=700,height=530)

        img_right = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\bg.jpg")
        img_right = img_right.resize((720, 100), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=80)

        #===============search system============================

        search_frame=LabelFrame(Right_frame,bd=2,bg="skyblue",relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        search_frame.place(x=0,y=80,width=697,height=70)

        Search_label=Label(search_frame,text="Search By",font=("times new roman",13,"bold"),bg="grey")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="read only",width=13) 
        search_combo["values"]=("Select","Roll_No","Phon_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=16,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey") 
        search_btn.grid(row=0,column=3,pady=5,padx=6)

        showAll_btn=Button(search_frame,text="Show All",width=12,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey") 
        showAll_btn.grid(row=0,column=4,pady=5,padx=6)

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="skyblue",relief=RIDGE)
        table_frame.place(x=0,y=160,width=697,height=350)

        scrollbar_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrollbar_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","Id","name","sec","roll","gender","dob","email","phone","address","subjectcode","photo"),xscrollcommand=scrollbar_x.set,yscrollcommand=scrollbar_y.set)
        scrollbar_x.pack(side=BOTTOM,fill=X)
        scrollbar_y.pack(side=RIGHT,fill=Y)
        scrollbar_x.config(command=self.student_table.xview)
        scrollbar_y.config(command=self.student_table.yview)


        self.student_table.heading("name",text="Name")
        self.student_table.heading("Id",text="Student Id")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("email",text="Semester")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("subjectcode",text="Subject Code")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("photo",text="Photo Samples Status")
        self.student_table["show"]="headings"

        self.student_table.column("name",width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("Id", width=100)
        self.student_table.column("sec", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("subjectcode", width=100)
        self.student_table.column("photo", width=122)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #======================function declaration=================

    def add_data(self):
        if self.var_dep.get() == "" or self.var_course.get() == "" or self.var_year.get() == "" or self.var_sem.get() == "" or self.var_std_Id.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),

                                                                                                    self.var_course.get(),

                                                                                                    self.var_year.get(),

                                                                                                    self.var_sem.get(),

                                                                                                    self.var_std_Id.get(),

                                                                                                    self.var_name.get(),

                                                                                                    self.var_section.get(),

                                                                                                    self.var_roll.get(),

                                                                                                    self.var_gender.get(),

                                                                                                    self.var_DOB.get(),

                                                                                                    self.var_email.get(),

                                                                                                    self.var_phone.get(),

                                                                                                    self.var_address.get(),

                                                                                                    self.var_subCode.get(),

                                                                                                    self.var_radio1.get()
                                                                                                    
                                                                                                    
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
    


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()



  #========================get cursor=======================
    def get_cursor(self, event=""):
        cursor_fouse = self.student_table.focus()
        contents = self.student_table.item(cursor_fouse)
        data = contents['values'] 


        self.var_dep.set(data[0])
        self.var_course.set(data[1])   
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_std_Id.set(data[4])
        self.var_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_section.set(data[7])
        self.var_gender.set(data[8])
        self.var_DOB.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_subCode.set(data[13])
        self.var_radio1.set(data[14])      

    def update_data(self):
       if self.var_dep.get() == "" or self.var_course.get() == "" or self.var_year.get() == "" or self.var_sem.get() == "" or self.var_std_Id.get() == "":
          messagebox.showerror("Error", "All fields are required",parent=self.root)   
       else:
           try:
               Update = messagebox.askyesno("Update", "Do you want to update this student details?",parent=self.root)
               if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                    UPDATE student SET 
                    Dep=%s,
                    Course=%s,
                    Year=%s,
                    Semester=%s,
                    Name=%s,
                    Section=%s,
                    Roll=%s,
                    Gender=%s,
                    DOB=%s,
                    Email=%s,
                    Phone=%s,
                    Address=%s,
                    Subject_code=%s,
                    PhotoSample=%s
                    WHERE Student_id=%s
                    """,(

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_section.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_DOB.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_subCode.get(),
                    self.var_radio1.get(),
                    self.var_std_Id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student record has been successfully updated", parent=self.root)
               else:
                    return
           except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)    
            
    # delete function
    def delete_data(self):
        if self.var_std_Id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)    
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_Id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()    
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    # reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_Id.set("")
        self.var_name.set("")
        self.var_section.set("")
        self.var_roll.set("")
        self.var_DOB.set("")
        self.var_gender.set("Male")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_subCode.set("")
        self.var_radio1.set("") 

      #=========================generate data set or take photo samples============================
    def generate_dataset(self):
        if self.var_dep.get() == "" or self.var_course.get() == "" or self.var_year.get() == "" or self.var_sem.get() == "" or self.var_std_Id.get() == "":
          messagebox.showerror("Error", "All fields are required",parent=self.root)   
        else:
            try:
               
                conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="face_recognition")
                my_cursor = conn.cursor()  
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()            
                id = 0
                for x in myresult:
                   id += 1
                my_cursor.execute("""
                    UPDATE student SET
                    Dep=%s,
                    Course=%s,
                    Year=%s,
                    Semester=%s,
                    Name=%s,
                    Section=%s,
                    Roll=%s,
                    Gender=%s,
                    DOB=%s,
                    Email=%s,
                    Phone=%s,
                    Address=%s,
                    Subject_code=%s,
                    PhotoSample=%s
                    WHERE Student_id=%s
                    """,(

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_section.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_DOB.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_subCode.get(),
                    self.var_radio1.get(),
                    self.var_std_Id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #======================Load predifiend data on face frontals from opencv===================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #scaling factor = 1.3
                    # Minimum Neighbour=5
                    for(x,y,w,h) in faces:
                        cropped_face = img[y:y + h, x:x + w]
                        return cropped_face
                    #return None
                cap=cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))  
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                       break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed successfully!")            
            
            except Exception as es:
               messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
            
if __name__ == "__main__":
      root = Tk()
      obj = Student(root)
      root.mainloop()
