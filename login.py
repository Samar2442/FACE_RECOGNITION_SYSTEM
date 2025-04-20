
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from main import Face_Recognition_System  # Ensure 'main.py' has a class named Face_Recognition_System

# Simulated user database
user_db = {"UIT": "1234"}


class Register_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("400x400+700+250")
        self.root.configure(bg="black")

        Label(self.root, text="Register", font=("times new roman", 20, "bold"), fg="white", bg="black").pack(pady=20)

        Label(self.root, text="Username:", font=("times new roman", 15), fg="white", bg="black").pack(pady=5)
        self.reg_user = Entry(self.root, font=("times new roman", 15))
        self.reg_user.pack(pady=5)

        Label(self.root, text="Password:", font=("times new roman", 15), fg="white", bg="black").pack(pady=5)
        self.reg_pass = Entry(self.root, show="*", font=("times new roman", 15))
        self.reg_pass.pack(pady=5)

        Button(self.root, text="Register", font=("times new roman", 12, "bold"),
               bg="red", fg="white", command=self.register_user).pack(pady=20)

    def register_user(self):
        username = self.reg_user.get()
        password = self.reg_pass.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif username in user_db:
            messagebox.showwarning("Warning", "User already exists", parent=self.root)
        else:
            user_db[username] = password
            messagebox.showinfo("Success", "Registered successfully", parent=self.root)
            self.root.destroy()

            # Launch main system after registration
            main_root = Toplevel()
            Face_Recognition_System(main_root)


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background image
        self.bg = ImageTk.PhotoImage(file=r"photo/11831.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=60)

        # Username
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=115)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=140, width=270)

        # Password
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=185)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=210, width=270)

        # Login Button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"),
                          bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=260, width=120, height=35)

        # Register Button
        registerbtn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"),
                             borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black",
                             command=self.open_register)
        registerbtn.place(x=15, y=310, width=160)

        # Forgot Password Button
        forgotbtn = Button(frame, text="Forgot Password", font=("times new roman", 10, "bold"),
                           borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgotbtn.place(x=15, y=340, width=160)

    def login(self):
        username = self.txtuser.get()
        password = self.txtpass.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
        elif username in user_db and user_db[username] == password:
            messagebox.showinfo("Success", "Welcome to our project FACE_RECOGNITION_SYSTEM")

            # Launch main system
            self.root.destroy()
            main_root = Tk()
            Face_Recognition_System(main_root)
            main_root.mainloop()

        else:
            messagebox.showerror("Invalid", "Invalid username or password")

    def open_register(self):
        self.new_window = Toplevel(self.root)
        Register_Window(self.new_window)


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
