from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os  
import csv
from tkinter import filedialog

mydata = []

class Attendance:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Text Variables
        self.attendanceId_var = StringVar()
        self.atten_roll_var = StringVar()
        self.attendance_name_var = StringVar()
        self.attend_dep_var = StringVar()
        self.attend_date_var = StringVar()
        self.attend_time_var = StringVar()
        self.atten_attendance_var = StringVar()
        


        # Title
        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT DESK", font=("times new roman", 35, "bold"), bg="lightgreen", fg="gray")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Background Image
        img_bottom = Image.open(r"college_images/attend.webp")
        img_bottom = img_bottom.resize((1530, 750), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        bg_lbl = Label(self.root, image=self.photoimg_bottom)
        bg_lbl.place(x=0, y=45, width=1530, height=750)
         
        main_frame = Frame(bg_lbl, bd=2, bg="light green")
        main_frame.place(x=20, y=130, width=1480, height=600)  # Adjusted the width and height

        # Left Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="skyblue", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 13, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=580)  # Adjusted the placement and size

        img_left = Image.open(r"college_images/train2.jpeg")
        img_left = img_left.resize((710, 100), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        left_lbl = Label(Left_frame, image=self.photoimg_left)
        left_lbl.place(x=5, y=0, width=710, height=100)  # Adjusted the placement and size

        
        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="light green")
        left_inside_frame.place(x=3, y=105, width=710, height=450) 

        #lable entry
        attendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("comicsansns 11 bold"),bg="skyblue")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        self.attendanceId_entry=ttk.Entry(left_inside_frame,textvariable=self.attendanceId_var,width=20,font=("comicsansns 11 bold"))
        self.attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        roll_label=Label(left_inside_frame,text="Roll:",font=("comicsansns 11 bold"),bg="skyblue")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        self.atten_roll=ttk.Entry(left_inside_frame,textvariable=self.atten_roll_var,width=20,font=("comicsansns 11 bold"))
        self.atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        name_label=Label(left_inside_frame,text="Name:",font=("comicsansns 11 bold"),bg="skyblue")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        self.attendance_name=ttk.Entry(left_inside_frame,textvariable=self.attendance_name_var,width=20,font=("comicsansns 11 bold"))
        self.attendance_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        dep_label=Label(left_inside_frame,text="Department:",font=("comicsansns 11 bold"),bg="skyblue")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        self.attend_dep_entry=ttk.Entry(left_inside_frame,textvariable=self.attend_dep_var,width=20,font=("comicsansns 11 bold"))
        self.attend_dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time
        time_label=Label(left_inside_frame,text="Time:",font=("comicsansns 11 bold"),bg="skyblue")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        self.time_attend=ttk.Entry(left_inside_frame,textvariable=self.attend_time_var,width=20,font=("comicsansns 11 bold"))
        self.time_attend.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        date_label=Label(left_inside_frame,text="Date:",font=("comicsansns 11 bold"),bg="skyblue")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        self.attend_date=ttk.Entry(left_inside_frame,textvariable=self.attend_date_var,width=20,font=("comicsansns 11 bold"))
        self.attend_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendance
        attendance_label=Label(left_inside_frame,text="Attendance status",font=("comicsansns 11 bold"),bg="skyblue")
        attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.atten_attendance_var,width=20,font=("comicsansns 11 bold"),state="read only") 
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,padx=2,pady=8)
        self.atten_status.current(0)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="skyblue")
        btn_frame.place(x=3,y=400,width=690,height=45)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCSV,width=15,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey") 
        save_btn.grid(row=0,column=0,pady=5,padx=6)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,width=15,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey")
        update_btn.grid(row=0,column=1,pady=5,padx=6)

        delete_btn=Button(btn_frame,text="Update CSV",width=15,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey") 
        delete_btn.grid(row=0,column=2,pady=5,padx=6)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,height=1,font=("times new roman",13,"bold"),bg="lightgreen",fg="grey") 
        reset_btn.grid(row=0,column=3,pady=5,padx=6)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="skyblue", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=740, y=10, width=720, height=580)  # Adjusted the placement and size

        # Adjusted the placement and size
        table_frame = Frame(Right_frame, bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5, y=0, width=700, height=455)

        #=========================scroll bar===========================
        scrollbar_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrollbar_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scrollbar_x.set,yscrollcommand=scrollbar_y.set)

        scrollbar_x.pack(side=BOTTOM,fill=X)
        scrollbar_y.pack(side=RIGHT,fill=Y)

        scrollbar_x.config(command=self.AttendanceReportTable.xview)
        scrollbar_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance Id")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #==================fetch data====================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCSV(self):
        global mydata
        mydata.clear()  # Clear existing data
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)        
        with open(filename) as myfile:
            csvreader = csv.reader(myfile)   
            for i in csvreader:
                mydata.append(i)
            self.fetchData(mydata) # i=row

    def exportCSV(self):
        try:
            if len(self.AttendanceReportTable.get_children()) < 1:   #self.AttendanceReportTable.get_children()
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                for row in self.AttendanceReportTable.get_children():
                    row_data = self.AttendanceReportTable.item(row)['values']
                    writer.writerow(row_data)
            messagebox.showinfo("Data Exported", "Your data has been exported to " + os.path.basename(filename)+"successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        contents = self.AttendanceReportTable.item(cursor_row)
        rows = contents['values']

        self.attendanceId_var.set(rows[0])        
        self.atten_roll_var.set(rows[1])   
        self.attendance_name_var.set(rows[2])
        self.attend_dep_var.set(rows[3])
        self.attend_time_var.set(rows[4])
        self.attend_date_var.set(rows[5])
        self.atten_attendance_var.set(rows[6]) 

    def reset_data(self):
        self.attendanceId_entry.delete(0, END)
        self.atten_roll.delete(0, END)
        self.attendance_name.delete(0, END)
        self.attend_dep_entry.delete(0, END)
        self.time_attend.delete(0, END)
        self.attend_date.delete(0, END)
        self.atten_status.set("Status")

    def update(self):
        selected_row = self.AttendanceReportTable.focus()  # Get the selected row
        values = self.AttendanceReportTable.item(selected_row, 'values')

        if not values:
            messagebox.showerror("Error", "Please select a record to update", parent=self.root)
            return

        # Retrieve updated data from entry fields
        attendance_id = self.attendanceId_var.get()
        roll = self.atten_roll_var.get()
        name = self.attendance_name_var.get()
        department = self.attend_dep_var.get()
        time = self.attend_time_var.get()
        date = self.attend_date_var.get()
        attendance_status = self.atten_attendance_var.get()

        # Update the selected row in the Treeview
        self.AttendanceReportTable.item(selected_row, values=(attendance_id, roll, name, department, time, date, attendance_status))

        # Optionally, you can update the data in your 'mydata' list as well, if it's used elsewhere in your application
        for idx, row in enumerate(mydata):
            if row == values:
                mydata[idx] = (attendance_id, roll, name, department, time, date, attendance_status)
                break

        messagebox.showinfo("Updated", "Record has been updated successfully", parent=self.root)
    


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
