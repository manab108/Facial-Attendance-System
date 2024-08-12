from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#import os
#from student import Student
#from train1 import Train
#from face_recognition import Face_Recognition
#from attendance import Attendance
#from developer import Developer
#from help import Help_desk
#from tkinter import messagebox
#import tkinter
#from datetime import datetime
#from time import strftime
#from tkinter import Label

class Face_Recognition_System:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #first image
        img = Image.open(r"C:\Users\Manab\Desktop\face recognition\college_images\image1.jpeg")
        img = img.resize((500, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=200)


        #second image
        img1 = Image.open(r"C:\Users\Manab\Desktop\face recognition\college_images\facialrecognition.png")
        img1 = img1.resize((500, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=200)


        # third image 
        img2 = Image.open(r"C:\Users\Manab\Desktop\face recognition\college_images\eye.jpg")
        img2 = img2.resize((500, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=200)

        #bg image
        img3 = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\bg.jpg")
        img3 = img3.resize((1500, 600), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1500, height=600)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 30, "bold"), bg="blue", fg="orange")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        #===================time button====================
         # Adding a label to display the time
        self.lbl = Label(title_lbl, font=("comic sans", 14, "bold"), background="blue", foreground="white")
        self.lbl.place(x=0, y=0, width=150, height=50)  # Adjust the placement and size as needed
        self.time()  # Call the time function to start the clock


 
        
        

         
        #student button
        img4 = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\221237a92d7420f35b91a275e181d5ea.jpg")
        img4 = img4.resize((150, 150), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details , cursor="hand2")
        b1.place(x=200, y=100, width=150, height=150)

        b1_1 = Button(bg_img, text="Student Details",command=self.student_details , cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=200, y=250, width=150, height=40)
        
         
        #detect face
        img5 = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\image34.jpg")
        img5 = img5.resize((150, 150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=150, height=150)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=500, y=250, width=150, height=40)

        #attendance
        img6 = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\attandance_sheet.jpg")
        img6 = img6.resize((150, 150), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=150, height=150)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=800, y=250, width=150, height=40)

        #help base
        img7 = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\customer_help.jpg")
        img7 = img7.resize((150, 150), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place(x=1100, y=100, width=150, height=150)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=1100, y=250, width=150, height=40)

        #Train faces button 
        img8 = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\train_faces.jpg")
        img8 = img8.resize((150, 150), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=350, width=150, height=150)

        b1_1 = Button(bg_img, text="Train Faces", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=200, y=500, width=150, height=40)

         #Photo faces button
        img9 = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((150, 150), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=350, width=150, height=150)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=500, y=500, width=150, height=40)
  
        
         #Developer button
        img10 = Image.open(r"C:\Users\alpha\OneDrive\Desktop\college_images\dev.jpg")
        img10 = img10.resize((150, 150), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,command=self.developer_data, cursor="hand2")
        b1.place(x=800, y=350, width=150, height=150)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=800, y=500, width=150, height=40)

         #Exit
        img11 = Image.open(r"college_images\Exit_button.jpg")
        img11 = img11.resize((150, 150), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.i_Exit)
        b1.place(x=1100, y=350, width=150, height=150)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.i_Exit, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=1100, y=500, width=150, height=40)

    def time(self):
        string = strftime('%H:%M:%S %p')
        self.lbl.config(text=string)
        self.lbl.after(1000, self.time)

    def open_img(self):
        os.startfile("data")

    def i_Exit(self):
         self.i_Exit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root)
         if self.i_Exit > 0:
           self.root.destroy()
         else:
           return    

         #==========================functions button=======================================
    def student_details(self):  
        self.new_window=Toplevel(self.root) 
        self.app=Student(self.new_window)

    def train_data(self):  
        self.new_window=Toplevel(self.root) 
        self.app=Train(self.new_window)   
    
    def face_data(self):  
        self.new_window=Toplevel(self.root) 
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Attendance(self.new_window)   

    def developer_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Help_desk(self.new_window)           




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()






