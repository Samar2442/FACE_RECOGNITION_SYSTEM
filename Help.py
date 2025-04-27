from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser
from tkinter import Label,Frame,Button
import logging
import os
import sys
from language import set_language, get_text  # Import language functions

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_label = Label(self.root, text="Help Desk", font=("times new roman", 35, "bold"), bg="grey", fg="blue")
        title_label.place(x=0, y=0, width=1530, height=60)

        # Background Image
        bg_image = Image.open(r"photo\man-working-call-center-office.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(bg_image)

        background_label = Label(self.root, image=self.photo_bg)
        background_label.place(x=0, y=60, width=1530, height=790)

        title_label = Label(self.root, text=get_text("help_desk"), font=("times new roman", 35, "bold"), bg="grey", fg="blue")
        title_label.place(x=0, y=0, width=1530, height=100)

        #home button
        img = Image.open(r"photo/beautiful-home_24877-50819.jpg")
        img = img.resize((70, 70), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        b1 = Button(title_label, image=self.photoimg, command=self.go_to_home, cursor="hand2")
        b1.place(x=10, y=0, width=70, height=70)

        self.home_button = Button(title_label, text=get_text("home"), command=self.go_to_home, cursor="hand2", font=("times new roman", 13, "bold"), bg="lavender", fg="black")
        self.home_button.place(x=10, y=70, width=70, height=30)


        # Background Image
        bg_image = Image.open(r"photo\man-working-call-center-office.jpg")
        bg_image = bg_image.resize((1530, 700), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(bg_image)

        background_label = Label(self.root, image=self.photo_bg)
        background_label.place(x=0, y=100, width=1530, height=700)

        # Email button
        b1_1 = Button(self.root, text="Email: abc12345@gmail.com", command=self.email, cursor="hand2",font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=415, y=300, width=700, height=70)

        # Call button
        b1_2 = Button(self.root, text="Call: 12345678910", command=self.call, cursor="hand2",font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_2.place(x=415, y=380, width=700, height=70)

    def email(self):
        try:
            webbrowser.open("https://mail.google.com/mail/?view=cm&fs=1&to=abc12345@gmail.com&su=Subject&body=Hello%20there")

        except Exception as e:
            messagebox.showerror("Error", f"Unable to open email client.\n{str(e)}")

    def call(self):
        messagebox.showinfo("Call", "Please call: 12345678910 from your mobile phone.")


    
    def change_language(self, event):
        selected_lang = self.language_combo.get()
        if selected_lang in self.language_map:
            set_language(self.language_map[selected_lang])
            self.update_texts()

    def update_texts(self):
        # Placeholder for actual text update logic
        self.title_label.config(text=get_text("help_desk"))
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

        
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
    
    
  