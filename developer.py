import cv2
import numpy as np
import threading
import mysql.connector
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

class Developer:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


         # Title
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="lightgreen", fg="gray")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Background Image
        img_bg = Image.open("college_images\developer.jpg")  # Update with your image path
        img_bg = img_bg.resize((1530, 750), Image.ANTIALIAS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        bg_lbl = Label(self.root, image=self.photoimg_bg)
        bg_lbl.place(x=0, y=45, width=1530, height=750)

         # Developer Frame
        main_frame = Frame(bg_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        img_top = Image.open("college_images\customer_help.jpg")  # Update with your image path
        img_top = img_top.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(main_frame, image=self.photoimg_top)
        f_lbl.place(x=300, y=0, width=200, height=200)

         # Developer Info
        dev_info = Label(main_frame, text="Hello!! I'm Neelam Kishor\nRole:Developer\nContact: baishyaneelam2@gmail.com",
                         font=("times new roman", 15, "bold"), bg="white", fg="black")
        dev_info.place(x=0, y=5)

        # More Developers (Add as needed)
        # Developer Image 2
        dev_img2 = Image.open("college_images/customer_help.jpg")  # Update with your image path
        dev_img2 = dev_img2.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_dev2 = ImageTk.PhotoImage(dev_img2)

        dev_img_lbl2 = Label(main_frame, image=self.photoimg_dev2, bg="white")
        dev_img_lbl2.place(x=20, y=250, width=200, height=200)

        # Developer Info 2
        dev_info2 = Label(main_frame, text="Developer Name: Jane Smith\nRole: Co-Developer\nContact: janesmith@example.com",
                          font=("times new roman", 15, "bold"), bg="white", fg="black")
        dev_info2.place(x=200, y=350)




if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()        