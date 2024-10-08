from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import numpy as np

class Train:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="lightgreen", fg="grey")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"college_images/train2.jpeg")
        img_top = img_top.resize((1530, 335), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=335)

        # Button
        b1_1 = Button(self.root, text="TRAIN DATA" ,command=self.train_classifier, cursor="hand2", font=("times new roman", 13, "bold"), bg="sky blue", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=40)

        img_bottom = Image.open(r"college_images/train1.webp")
        img_bottom = img_bottom.resize((1530, 370), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=420, width=1530, height=370)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image_path in path:
            img = Image.open(image_path).convert('L')  # Grey scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image_path)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training", imageNp)
            if cv2.waitKey(1) == 13:  # Break on pressing Enter key
                break

        ids = np.array(ids)

        # Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Data Set complete!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
