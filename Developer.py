from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import Label,Frame
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import Label, Frame
from PIL import Image, ImageTk
import logging
import os
import sys
from language import set_language, get_text  # Import language functions


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_label = Label(
            self.root,
            text="Team Loosars Developers",

            text=get_text("developer"),  # Use dynamic text from language file

            font=("times new roman", 35, "bold"),
            bg="grey",
            fg="blue"
        )
        title_label.place(x=0, y=0, width=1530, height=60)

        title_label.place(x=0, y=0, width=1530, height=100)

        #home button
        img = Image.open(r"photo/beautiful-home_24877-50819.jpg")
        img = img.resize((70, 70), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        b1 = Button(title_label, image=self.photoimg, command=self.go_to_home, cursor="hand2")
        b1.place(x=10, y=0, width=70, height=70)

        self.home_button = Button(title_label, text=get_text("Home"), command=self.go_to_home, cursor="hand2", font=("times new roman", 13, "bold"), bg="lavender", fg="black")
        self.home_button.place(x=10, y=70, width=70, height=30)


        # Background Image
        bg_image = Image.open(r"photo\devaloper.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(bg_image)

        background_label = Label(self.root, image=self.photo_bg)

        background_label.place(x=0, y=60, width=1530, height=790)

        background_label.place(x=0, y=100, width=1530, height=700)

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



        self.dev1_status_label = Label(dev1_frame, text=get_text("team_admin"), font=("times new roman", 20, "bold"), bg="lavender", fg="blue", wraplength=330, justify="center")
        self.dev1_status_label.place(relx=0.5, y=255, anchor="n")

        self.dev1_name_label = Label(dev1_frame, text=get_text("NAME : Aditya Roy"), font=("times new roman", 20, "bold"), bg="lavender", fg="blue")
        self.dev1_name_label.place(x=5, y=295)

        self.dev1_dept_label = Label(dev1_frame, text=get_text("DEPT : Information Technology"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue")
        self.dev1_dept_label.place(x=5, y=335)

        self.dev1_year_label = Label(dev1_frame, text=get_text("Year : 1st Year"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue")
        self.dev1_year_label.place(x=5, y=375)

        self.dev1_college_label = Label(dev1_frame, text=get_text("College : University Institute of Technology,BU"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue", wraplength=330, justify="center")
        self.dev1_college_label.place(x=5, y=415)

        # Developer 2 Frame
        dev2_frame = Frame(background_label, bd=2, bg="lavender")
        dev2_frame.place(x=395, y=110, width=350, height=500)

        dev2_image = Image.open(r"photo\Somoresh.jpg")

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

        self.dev2_status_label = Label(dev2_frame, text=get_text("team_member"), font=("times new roman", 20, "bold"), bg="lavender", fg="blue", wraplength=330, justify="center")
        self.dev2_status_label.place(relx=0.5, y=255, anchor="n")

        self.dev2_name_label = Label(dev2_frame, text=get_text("NAME : Samaresh Debnath"), font=("times new roman", 20, "bold"), bg="lavender", fg="blue")
        self.dev2_name_label.place(x=5, y=295)

        self.dev2_dept_label = Label(dev2_frame, text=get_text("DEPT : Information Technology"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue")
        self.dev2_dept_label.place(x=5, y=335)

        self.dev2_year_label = Label(dev2_frame, text=get_text("Year : 1st Year"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue")
        self.dev2_year_label.place(x=5, y=375)

        self.dev2_college_label = Label(dev2_frame, text=get_text("College : University Institute of Technology,BU"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue", wraplength=330, justify="center")
        self.dev2_college_label.place(x=5, y=415)

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


        self.dev3_status_label = Label(dev3_frame, text=get_text("team_member"), font=("times new roman", 20, "bold"), bg="lavender", fg="blue", wraplength=330, justify="center")
        self.dev3_status_label.place(relx=0.5, y=255, anchor="n")

        self.dev3_name_label = Label(dev3_frame, text=get_text("NAME : Subhasis Mahato"), font=("times new roman", 20, "bold"), bg="lavender", fg="blue")
        self.dev3_name_label.place(x=5, y=295)

        self.dev3_dept_label = Label(dev3_frame, text=get_text("DEPT : Information Technology"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue")
        self.dev3_dept_label.place(x=5, y=335)

        self.dev3_year_label = Label(dev3_frame, text=get_text("Year : 1st Year"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue")
        self.dev3_year_label.place(x=5, y=375)

        self.dev3_college_label = Label(dev3_frame, text=get_text("College : University Institute of Technology,BU"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue", wraplength=330, justify="center")
        self.dev3_college_label.place(x=5, y=415)

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




        self.dev4_status_label = Label(dev4_frame, text=get_text("team_member"), font=("times new roman", 20, "bold"), bg="lavender", fg="blue", wraplength=330, justify="center")
        self.dev4_status_label.place(relx=0.5, y=255, anchor="n")

        self.dev4_name_label = Label(dev4_frame, text=get_text("NAME : Deepanjan Seth"), font=("times new roman", 20, "bold"), bg="lavender", fg="blue")
        self.dev4_name_label.place(x=5, y=295)

        self.dev4_dept_label = Label(dev4_frame, text=get_text("DEPT : Information Technology"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue")
        self.dev4_dept_label.place(x=5, y=335)

        self.dev4_year_label = Label(dev4_frame, text=get_text("Year : 1st Year"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue")
        self.dev4_year_label.place(x=5, y=375)

        self.dev4_college_label = Label(dev4_frame, text=get_text("College : University Institute of Technology,BU"), font=("times new roman", 18, "bold"), bg="lavender", fg="blue", wraplength=330, justify="center")
        self.dev4_college_label.place(x=5, y=415)

    def change_language(self, event):
        selected_lang = self.language_combo.get()
        if selected_lang in self.language_map:
            set_language(self.language_map[selected_lang])
            self.update_texts()

    def update_texts(self):
        # Placeholder for actual text update logic
        self.dev1_status_label.config(text=get_text("status"))
        self.dev1_name_label.config(text=get_text("name"))
        self.dev1_dept_label.config(text=get_text("dept"))
        self.dev1_year_label.config(text=get_text("year"))
        self.dev1_college_label.config(text=get_text("college"))

        self.dev2_status_label.config(text=get_text("status"))
        self.dev2_name_label.config(text=get_text("name"))
        self.dev2_dept_label.config(text=get_text("dept"))
        self.dev2_year_label.config(text=get_text("year"))
        self.dev2_college_label.config(text=get_text("college"))

        self.dev3_status_label.config(text=get_text("status"))
        self.dev3_name_label.config(text=get_text("name"))
        self.dev3_dept_label.config(text=get_text("dept"))
        self.dev3_year_label.config(text=get_text("year"))
        self.dev3_college_label.config(text=get_text("college"))

        self.dev4_status_label.config(text=get_text("status"))
        self.dev4_name_label.config(text=get_text("name"))
        self.dev4_dept_label.config(text=get_text("dept"))
        self.dev4_year_label.config(text=get_text("year"))
        self.dev4_college_label.config(text=get_text("college"))

        self.home_button.config(text=get_text("home"))
        
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

logging.basicConfig(level=logging.INFO)

# Example of language change
set_language("hi")  # Change language to Hindi
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()