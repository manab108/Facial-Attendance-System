from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train1 import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer


class Help_desk:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

         # Title
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="black", fg="light green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Background Image
        img_bg = Image.open("college_images\developer.jpg")  # Update with your image path
        img_bg = img_bg.resize((1530, 750), Image.ANTIALIAS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        bg_lbl = Label(self.root, image=self.photoimg_bg)
        bg_lbl.place(x=0, y=45, width=1530, height=750)

        # Developer Info
        dev_info = Label(bg_lbl, text="Email: baishyaneelam2@gmail.com",
                         font=("times new roman", 15, "bold"), bg="white", fg="black")
        dev_info.place(x=600, y=220)

if __name__ == "__main__":
    root = Tk()
    obj = Help_desk(root)
    root.mainloop()        