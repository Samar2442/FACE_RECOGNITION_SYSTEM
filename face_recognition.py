from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime
import logging
import os
import sys
from language import set_language, get_text  # Import language functions



class Face_recognition:
    def __init__(self, root): 
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

        # Title label
        self.title_lbl = Label(self.root, text=get_text('face_recognition'), font=("times new roman", 30, "bold"), bg="grey", fg="blue")
        self.title_lbl.place(x=0, y=0, width=1530, height=100)

        # Home button
        img = Image.open(r"photo/beautiful-home_24877-50819.jpg")
        img = img.resize((70, 70), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        b1 = Button(self.title_lbl, image=self.photoimg, command=self.go_to_home, cursor="hand2")
        b1.place(x=10, y=0, width=70, height=70)

        self.home_button = Button(self.title_lbl, text=get_text("home"), command=self.go_to_home, cursor="hand2", font=("times new roman", 13, "bold"), bg="lavender", fg="black")
        self.home_button.place(x=10, y=70, width=70, height=30)


        img_top = Image.open(r"photo\1_RZc0lk7gkMGXv6nEOwc7Ng.jpg")
        img_top = img_top.resize((1530, 325), Image.FIXED)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        top_img_label = Label(self.root, image=self.photoimg_top)
        top_img_label.place(x=0, y=100, width=650, height=700)

        # Left image
        img_left = Image.open(r"photo\2401770.jpg")
        img_left = img_left.resize((650, 325), Image.FIXED)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        left_img_label = Label(self.root, image=self.photoimg_left)
        left_img_label.place(x=650, y=100, width=950, height=700)

        # Button frame
        self.b1_1=Button(left_img_label, text=get_text("face_recognition"), command=self.face_recognition,  font=("times new roman", 15, "bold"), bg="blue", fg="white")
        self.b1_1.place(x=350, y=550, width=200, height=45)

        #exit button
        self.b1_2=Button(left_img_label, text=get_text("exit"), command=self.root.destroy,  font=("times new roman", 15, "bold"), bg="blue", fg="white")
        self.b1_2.place(x=350, y=600, width=200, height=45)

    #attendance button
    def attendance(self,i,r,d,n):
        with open("attendance.csv", "r++", newline="/n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if (i not in name_list) and (r not in name_list) and (d not in name_list) and (n not in name_list):
                now = datetime.now()
                d1= now.strftime("%d:%m:%Y")
                dt_string = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{d},{n},{dt_string},{d1},Present")
            else:
                messagebox.showinfo("Attendance", "Already Marked Attendance")



    #face recognition 

    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
            coords = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="face recognition system")
                my_cursor = conn.cursor()

                my_cursor.execute("select Student_ID from student where Student_ID=" + str(id))
                id = my_cursor.fetchone()
                id = "+".join(id) if id else "Unknown"

                my_cursor.execute("select Name from student where Student_ID=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("select Roll from student where Student_ID=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("select Dep from student where Student_ID=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"
    
                if confidence > 77:
                    cv2.putText(img, f"ID: {id}", (x, y - 70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Dep: {d}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.attendance(id, r, d, n)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                coords = [x, y, w, h]
            return coords

        def recognize(img, clf, faceCascade):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_capture.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter key to exit
                break

        video_capture.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Face Recognition Completed")
    
    # Exit function
    def exit(self):
        self.root.destroy()

    def change_language(self, event):
        selected_lang = self.language_combo.get()
        if selected_lang in self.language_map:
            set_language(self.language_map[selected_lang])
            self.update_texts()

    def update_texts(self):
        # Placeholder for actual text update logic
        self.title_lbl.config(text=get_text("face_recognition"))
        self.home_button.config(text=get_text("home"))
        self.b1_1.config(text=get_text("face_recognition"))
        self.b1_2.config(text=get_text("exit"))


    def go_to_home(self):
        """This method will close the current Developer window and open the main application window."""
        self.root.destroy()  # Close the current Developer window
        self.open_main_window()  # Open the main application window

    def open_main_window(self):
        """Opens the main window (main.py)"""
        try:
            import main  # Import your main window module here
            main.main()  # Assuming `main.py` has a `main()` function to start the app
        except ImportError:
            logging.error("Error importing the main window module. Ensure 'main.py' exists.")



if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
