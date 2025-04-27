from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk
from tkinter import Label,Frame,Button,Toplevel

from tkinter import Label, Frame, Button, Toplevel
from student import Student
from Developer import Developer
from time import strftime
from datetime import datetime
from Train import Train
from Help import Help

from chatbot import Chatbot
from Help import Help
# from Attendence import Attendence
import os
from face_recognition import Face_recognition
from language import get_text, set_language



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

        set_language("en")

        # First image
        img = Image.open(r"photo/face-recognition-personal-identification-collage (4).jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"photo/face-recognition-personal-identification-collage.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg2)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"photo/face-recognition-personal-identification-collage (3).jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg3)
        f_lbl2.place(x=1000, y=0, width=500, height=130)

        # Background image
        img3 = Image.open(r"photo/11831.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)
       
        # Title label       
        title_lbl = Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SYSTEM  SOFTWARE", font=("times new roman", 30, "bold"), bg="lavender", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman", 14, "bold"),background='lavender',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)


        # Title label
        self.title_lbl = Label(bg_img, text=get_text("title"), font=("times new roman", 30, "bold"), bg="lavender", fg="blue")
        self.title_lbl.place(x=0, y=0, width=1530, height=45)

        # time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(self.title_lbl, font=("times new roman", 14, "bold"), background='lavender', foreground='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # student button
        img4 = Image.open(r"photo/group-young-students-front-school-building.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=100, y=100, width=220, height=220)

        self.student_text_button = Button(bg_img, text=get_text("Student Details"), command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.student_text_button.place(x=100, y=300, width=220, height=40)

        # detect face button
        img5 = Image.open(r"photo/face-recognition-personal-identification-collage (2).jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.face_data)
        b1.place(x=400, y=100, width=220, height=220)

        self.face_detector_text_button = Button(bg_img, text=get_text("Face Detector"), cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white", command=self.face_data)
        self.face_detector_text_button.place(x=400, y=300, width=220, height=40)

        # attendance button
        img6 = Image.open(r"photo/Choosing-The-Right-Attendance-Management-System.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=700, y=100, width=220, height=220)

        self.attendance_text_button = Button(bg_img, text=get_text("Attendance"), cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.attendance_text_button.place(x=700, y=300, width=220, height=40)

        # Language change section
        dev1_frame = Frame(bg_img, bd=2, bg="lavender")
        dev1_frame.place(x=1270, y=70, width=270, height=35)

        self.language_label = Label(dev1_frame, text=get_text("Language"), font=("times new roman", 12, "bold"), bg="lavender")
        self.language_label.grid(row=1, column=1, padx=1, sticky=W)

        self.language_combo = ttk.Combobox(dev1_frame, font=("times new roman", 10, "bold"), state="readonly")
        self.language_combo["values"] = ("Select Language", "English", "Hindi", "Bengali", "Tamil", "Telugu", "Gujarati")
        self.language_combo.current(0)
        self.language_combo.grid(row=1, column=2, padx=2, pady=5, sticky=W)

        # Mapping the languages to codes
        self.language_map = {
            "Select Language":"en",
            "English": "en",
            "Hindi": "hi",
            "Bengali": "bn",
            "Tamil": "ta",
            "Telugu": "te",
            "Gujarati": "gu"
        }

        # Bind combobox selection event
        self.language_combo.bind("<<ComboboxSelected>>", self.change_language)

        # chat box button
        img7 = Image.open(r"photo/man-working-call-center-office.jpg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.help)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)
        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.chatbot)
        b1.place(x=1000, y=100, width=220, height=220)

        self.chatbox_text_button = Button(bg_img, text=get_text("Chat Box"), cursor="hand2", command=self.chatbot, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.chatbox_text_button.place(x=1000, y=300, width=220, height=40)

        # train button
        img8 = Image.open(r"photo/gps-system-smart-car.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.train_data)
        b1.place(x=100, y=380, width=220, height=220)

        self.train_data_text_button = Button(bg_img, text=get_text("Train Data"), cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.train_data_text_button.place(x=100, y=580, width=220, height=40)

        # photo button
        img9 = Image.open(r"photo/close-up-man-robotic-process-automation-concept.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.open_img)
        b1.place(x=400, y=380, width=220, height=220)

        self.photo_text_button = Button(bg_img, text=get_text("Photos"), cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.photo_text_button.place(x=400, y=580, width=220, height=40)

       # developer button
        img10 = Image.open(r"photo/devaloper.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img10)

        self.developer_button = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.developer_data)
        self.developer_button.place(x=700, y=380, width=220, height=220)

        self.developer_text_button = Button(bg_img, text=get_text("Developer"), cursor="hand2", command=self.developer_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.developer_text_button.place(x=700, y=580, width=220, height=40)

        # exit button
        img11 = Image.open(r"photo/escape-concept-illustration_114360-5786.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img11)
        
        b1 = Button(bg_img, image=self.photoimg12, cursor="hand2",command=self.exit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.exit, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)
    

        self.exit_button = Button(bg_img, image=self.photoimg12, cursor="hand2", command=self.exit)
        self.exit_button.place(x=1000, y=380, width=220, height=220)

        self.exit_text_button = Button(bg_img, text=get_text("Exit"), cursor="hand2", command=self.exit, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.exit_text_button.place(x=1000, y=580, width=220, height=40)

        # help button
        img12 = Image.open(r"photo/man-working-call-center-office.jpg")
        img12 = img12.resize((220, 200), Image.Resampling.LANCZOS)
        self.photoimg13 = ImageTk.PhotoImage(img12)

        self.help_button = Button(bg_img, image=self.photoimg13, cursor="hand2", command=self.help)
        self.help_button.place(x=1280, y=250, width=220, height=220)

        self.help_text_button = Button(bg_img, text=get_text("Help"), cursor="hand2", command=self.help, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.help_text_button.place(x=1280, y=450, width=220, height=40)


    def open_img(self):
        os.startfile("data")

    def exit(self):
        self.exit=messagebox.askyesno("Face Recognition","Do you want to exit the project?")
        if self.exit >0:
        self.exit = messagebox.askyesno("Face Recognition", "Do you want to exit the project?")
        if self.exit > 0:
            self.root.destroy()
        else:
            return


    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def chatbot(self):
        self.new_window = Toplevel(self.root)
        self.app = Chatbot(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



    # def attendance_data(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = Attendence(self.new_window)

    def change_language(self, event):
        selected_lang = self.language_combo.get()
        if selected_lang in self.language_map:
            set_language(self.language_map[selected_lang])
            self.update_texts()

    def update_texts(self):
        # Placeholder for actual text update logic
        self.title_lbl.config(text=get_text("title"))
        self.student_text_button.config(text=get_text("student_details"))
        self.face_detector_text_button.config(text=get_text("face_detector"))
        self.attendance_text_button.config(text=get_text("attendance"))
        self.language_label.config(text=get_text("language"))
        self.chatbox_text_button.config(text=get_text("chatbox"))
        self.train_data_text_button.config(text=get_text("train_data"))
        self.photo_text_button.config(text=get_text("photos"))
        self.developer_text_button.config(text=get_text("developer"))
        self.exit_text_button.config(text=get_text("exit"))
        self.help_text_button.config(text=get_text("help"))

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


    


if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()

