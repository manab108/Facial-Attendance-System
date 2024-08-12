import cv2
import numpy as np
import threading
import mysql.connector
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNIZER", font=("times new roman", 35, "bold"), bg="lightgreen", fg="gray")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_bottom = Image.open(r"college_images\image1.jpeg")
        img_bottom = img_bottom.resize((1530, 750), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=45, width=1530, height=750)

        # button
        b1_1 = Button(f_lbl, text="FACE RECOGNITION", cursor="hand2", font=("times new roman", 20, "bold"), bg="grey", fg="light green", command=self.start_face_recog)
        b1_1.place(x=10, y=50, width=370, height=90)

    def mark_attendance(self, i, r, n, d):
        if i == "Unknown" or r == "Unknown" or n == "Unknown" or d == "Unknown":
            return

        with open("neelam.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                if len(entry) > 0:
                    name_list.append(entry[0])
            if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    def start_face_recog(self):
        # Start face recognition in a separate thread
        threading.Thread(target=self.face_recog).start()

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                if confidence > 77:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="face_recognition")
                    my_cursor = conn.cursor()

                    my_cursor.execute("SELECT Name FROM student WHERE Student_id = %s", (str(id),))
                    n = my_cursor.fetchone()
                    n = n[0] if n else "Unknown"

                    my_cursor.execute("SELECT Roll FROM student WHERE Student_id = %s", (str(id),))
                    r = my_cursor.fetchone()
                    r = r[0] if r else "Unknown"

                    my_cursor.execute("SELECT Dep FROM student WHERE Student_id = %s", (str(id),))
                    d = my_cursor.fetchone()
                    d = d[0] if d else "Unknown"

                    my_cursor.execute("SELECT Student_id FROM student WHERE Student_id = %s", (str(id),))
                    i = my_cursor.fetchone()
                    i = i[0] if i else "Unknown"
                    
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                    # Mark attendance only for recognized faces
                    self.mark_attendance(i, r, n, d)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Person", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)

                coord = [x, y, w, h]

            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
