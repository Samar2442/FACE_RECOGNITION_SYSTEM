from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser
from tkinter import Label,Frame,Button
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

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
