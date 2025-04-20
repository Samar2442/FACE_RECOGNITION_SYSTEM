from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import Label,Frame
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_label = Label(
            self.root,
            text="Team Loosars Developers",
            font=("times new roman", 35, "bold"),
            bg="grey",
            fg="blue"
        )
        title_label.place(x=0, y=0, width=1530, height=60)

        # Background Image
        bg_image = Image.open(r"photo\devaloper.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(bg_image)

        background_label = Label(self.root, image=self.photo_bg)
        background_label.place(x=0, y=60, width=1530, height=790)

        # Developer 1 Frame
        dev1_frame = Frame(background_label, bd=2, bg="lavender")
        dev1_frame.place(x=0, y=110, width=350, height=500)

        dev1_image = Image.open(r"photo\Aditya.jpg")
        dev1_image = dev1_image.resize((350, 250), Image.LANCZOS)
        self.photo_dev1 = ImageTk.PhotoImage(dev1_image)

        dev1_image_label = Label(dev1_frame, image=self.photo_dev1)
        dev1_image_label.place(x=0, y=0, width=350, height=250)

        dev1_status_label = Label(dev1_frame,text="TEAM ADMIN",font=("times new roman", 20, "bold"),bg="lavender",fg="blue", wraplength=330,justify="center")
        dev1_status_label.place(relx=0.5, y=255, anchor="n")

        dev1_name_label = Label(dev1_frame,text="NAME : Aditya Roy",font=("times new roman", 20, "bold"),bg="lavender",fg="blue")
        dev1_name_label.place(x=5, y=295)

        dev1_dept_label = Label(dev1_frame,text="DEPT : Information Technology",font=("times new roman", 18, "bold"),bg="lavender",fg="blue")
        dev1_dept_label.place(x=5, y=335)

        dev1_year_label = Label(dev1_frame,text="Year : 1st Year",font=("times new roman", 18, "bold"),bg="lavender",fg="blue")
        dev1_year_label.place(x=5, y=375)

        dev1_college_label = Label(dev1_frame,text="College : University Institute of Technology,BU",font=("times new roman", 18, "bold"),bg="lavender",fg="blue",wraplength=330,justify="center")
        dev1_college_label.place(x=5, y=415)



        # Developer 2 Frame
        dev2_frame = Frame(background_label, bd=2, bg="lavender")
        dev2_frame.place(x=395, y=110, width=350, height=500)

        dev2_image = Image.open(r"photo\Samaresh.jpg")
        dev2_image = dev2_image.resize((350, 250), Image.LANCZOS)
        self.photo_dev2 = ImageTk.PhotoImage(dev2_image)

        dev2_image_label = Label(dev2_frame, image=self.photo_dev2)
        dev2_image_label.place(x=0, y=0, width=350, height=250)

        dev2_status_label = Label(dev2_frame,text="TEAM MEMBER",font=("times new roman", 20, "bold"),bg="lavender",fg="blue", wraplength=330,justify="center")
        dev2_status_label.place(relx=0.5, y=255, anchor="n")

        dev2_name_label = Label(dev2_frame,text="NAME : Samaresh Debnath",font=("times new roman", 20, "bold"),bg="lavender",fg="blue")
        dev2_name_label.place(x=5, y=295)

        dev2_dept_label = Label(dev2_frame,text="DEPT : Information Technology",font=("times new roman", 18, "bold"),bg="lavender",fg="blue")
        dev2_dept_label.place(x=5, y=335)

        dev2_year_label = Label(dev2_frame,text="Year : 1st Year",font=("times new roman", 18, "bold"),bg="lavender",fg="blue")
        dev2_year_label.place(x=5, y=375)

        dev2_college_label = Label(dev2_frame,text="College : University Institute of Technology,BU",font=("times new roman", 18, "bold"),bg="lavender",fg="blue",wraplength=330,justify="center")
        dev2_college_label.place(x=5, y=415)

        # Developer 3 Frame
        dev3_frame = Frame(background_label, bd=2, bg="lavender")
        dev3_frame.place(x=790, y=110, width=350, height=500)

        dev3_image = Image.open(r"photo\Subhasis.jpg")
        dev3_image = dev3_image.resize((350, 250), Image.LANCZOS)
        self.photo_dev3 = ImageTk.PhotoImage(dev3_image)

        dev3_image_label = Label(dev3_frame, image=self.photo_dev3)
        dev3_image_label.place(x=0, y=0, width=350, height=250)

        dev3_status_label = Label(dev3_frame,text="TEAM MEMBER",font=("times new roman", 20, "bold"),bg="lavender",fg="blue", wraplength=330,justify="center")
        dev3_status_label.place(relx=0.5, y=255, anchor="n")

        dev3_name_label = Label(dev3_frame,text="NAME : Subhasis Mahato",font=("times new roman", 20, "bold"),bg="lavender",fg="blue")
        dev3_name_label.place(x=5, y=295)

        dev3_dept_label = Label(dev3_frame,text="DEPT : Information Technology",font=("times new roman", 18, "bold"),bg="lavender",fg="blue")
        dev3_dept_label.place(x=5, y=335)

        dev3_year_label = Label(dev3_frame,text="Year : 1st Year",font=("times new roman", 18, "bold"),bg="lavender",fg="blue")
        dev3_year_label.place(x=5, y=375)

        dev3_college_label = Label(dev3_frame,text="College : University Institute of Technology,BU",font=("times new roman", 18, "bold"),bg="lavender",fg="blue",wraplength=330,justify="center")
        dev3_college_label.place(x=5, y=415)


        # Developer 4 Frame
        dev4_frame = Frame(background_label, bd=2, bg="lavender")
        dev4_frame.place(x=1180, y=110, width=350, height=500)

        dev4_image = Image.open(r"photo\Deepanjan.jpg")
        dev4_image = dev4_image.resize((350, 250), Image.LANCZOS)
        self.photo_dev4 = ImageTk.PhotoImage(dev4_image)

        dev4_image_label = Label(dev4_frame, image=self.photo_dev4)
        dev4_image_label.place(x=0, y=0, width=350, height=250)

        dev4_status_label = Label(dev4_frame,text="TEAM MEMBER",font=("times new roman", 20, "bold"),bg="lavender",fg="blue", wraplength=330,justify="center")
        dev4_status_label.place(relx=0.5, y=255, anchor="n")

        dev4_name_label = Label(dev4_frame,text="NAME : Deepanjan Seth",font=("times new roman", 20, "bold"),bg="lavender",fg="blue")
        dev4_name_label.place(x=5, y=295)

        dev4_dept_label = Label(dev4_frame,text="DEPT : Information Technology",font=("times new roman", 18, "bold"),bg="lavender",fg="blue")
        dev4_dept_label.place(x=5, y=335)

        dev4_year_label = Label(dev4_frame,text="Year : 1st Year",font=("times new roman", 18, "bold"),bg="lavender",fg="blue")
        dev4_year_label.place(x=5, y=375)

        dev4_college_label = Label(dev4_frame,text="College : University Institute of Technology,BU",font=("times new roman", 18, "bold"),bg="lavender",fg="blue",wraplength=330,justify="center")
        dev4_college_label.place(x=5, y=415)



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
