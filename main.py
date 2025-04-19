from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk
from tkinter import Label,Frame,Button,Toplevel
from student import Student
from Developer import Developer
from Train import Train
from Help import Help
import os

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")


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
        title_lbl = Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SYSTEM  SOFTWARE", font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        

        # student button
        img4 = Image.open(r"photo/group-young-students-front-school-building.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # detect face button
        img5 = Image.open(r"photo/face-recognition-personal-identification-collage (2).jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)
        
        # attendance button
        img6 = Image.open(r"photo/Choosing-The-Right-Attendance-Management-System.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img6)
        
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        # help button
        img7 = Image.open(r"photo/man-working-call-center-office.jpg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.help)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # train button
        img8 = Image.open(r"photo/gps-system-smart-car.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

        #photo button
        img9 = Image.open(r"photo/close-up-man-robotic-process-automation-concept.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2" , command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

        # developer button
        img10 = Image.open(r"photo/devaloper.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.developer_data)
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

        # exit button
        img11 = Image.open(r"photo/escape-concept-illustration_114360-5786.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img11)
        
        b1 = Button(bg_img, image=self.photoimg12, cursor="hand2",command=self.exit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.exit, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)
    
    def open_img(self):
        os.startfile("data")

    def exit(self):
        self.exit=messagebox.askyesno("Face Recognition","Do you want to exit the project?")
        if self.exit >0:
            self.root.destroy()
        else:
            return

    # Functionality buttons
    def student_details(self):
         self.new_window = Toplevel(self.root)
         self.app = Student(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()

