from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")
        
        #variable
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_class_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher_name = StringVar()


        # First image
        img = Image.open("photo/istockphoto-1430114131-612x612.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)


        # Second image
        img1 = Image.open("photo/istockphoto-1307457391-612x612.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg2)
        f_lbl1.place(x=500, y=0, width=500, height=130)


        # Third image
        img2 = Image.open("photo/pexels-hillaryfox-1595391.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)
        
        f_lbl2 = Label(self.root, image=self.photoimg3)
        f_lbl2.place(x=1000, y=0, width=500, height=130)

        
        # Background image
        img3 = Image.open("photo/GettyImages-1072191138.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)
       
        # Title label       
        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)

        # Left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief="ridge", text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)

        # Left frame image
        img_left = Image.open("photo/GettyImages-1072191138.jpg")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        left_frame_img = Label(left_frame, image=self.photoimg_left)
        left_frame_img.place(x=5, y=0, width=720, height=120)

        #current course
        current_course_label = LabelFrame(left_frame, text="Current Course Information", bg="white", relief="ridge", font=("times new roman", 12, "bold"))
        current_course_label.place(x=5, y=124, width=720, height=115)
        #department label
        dep_label = Label(current_course_label, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_label, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "CSE", "IT", "ME", "CE","ECE", "EE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course label
    
        course_label = Label(current_course_label, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_label, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "B.E", "B.Tech", "M.E", "M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)


        # Year label
        year_label = Label(current_course_label, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        
        year_combo = ttk.Combobox(current_course_label, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester label
        semester_label = Label(current_course_label, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_label, textvariable=self.var_sem, font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "1st Semester", "2nd Semester", "3rd Semester", "4th Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        

        # Student information label
        student_info_label = LabelFrame(left_frame, text="Student Information", bg="white", relief="ridge", font=("times new roman", 12, "bold"))
        student_info_label.place(x=5, y=240, width=720, height=315)

        # Student ID label
        student_id_label = Label(student_info_label, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10, sticky=W)

        student_id_entry = ttk.Entry(student_info_label, textvariable=self.var_id, font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Student name label
        student_name_label = Label(student_info_label, text="Student Name", font=("times new roman", 12, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10, sticky=W)

        student_name_entry = ttk.Entry(student_info_label, textvariable=self.var_name, font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # class devision label
        class_div_label = Label(student_info_label, text="Class Division", font=("times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, sticky=W)

        class_div_combo = ttk.Combobox(student_info_label, textvariable=self.var_class_div, font=("times new roman", 12, "bold"), state="readonly", width=18)
        class_div_combo["values"] = ("Select Class Division", "A", "B", "C", "D")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Roll no label
        roll_no_label = Label(student_info_label, text="Roll No", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, sticky=W)

        roll_no_entry = ttk.Entry(student_info_label, textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #gender label
        gender_label = Label(student_info_label, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(student_info_label, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        #dob label
        dob_label = Label(student_info_label, text="Date of Birth", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, sticky=W)

        dob_entry = ttk.Entry(student_info_label, textvariable=self.var_dob, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # email label
        email_label = Label(student_info_label, text="Email", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, sticky=W)

        email_entry = ttk.Entry(student_info_label, textvariable=self.var_email, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        # phone label
        phone_label = Label(student_info_label, text="Phone No", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, sticky=W)

        phone_entry = ttk.Entry(student_info_label, textvariable=self.var_phone, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=2, pady=10, sticky=W)

        # address label
        address_label = Label(student_info_label, text="Address", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, sticky=W)

        address_entry = ttk.Entry(student_info_label, textvariable=self.var_address, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=2, pady=10, sticky=W)

        # teacher name label
        teacher_name_label = Label(student_info_label, text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
        teacher_name_label.grid(row=4, column=2, padx=10, sticky=W)

        teacher_name_entry = ttk.Entry(student_info_label, textvariable=self.var_teacher_name, font=("times new roman", 12, "bold"))
        teacher_name_entry.grid(row=4, column=3, padx=2, pady=10, sticky=W)

        #radio button
        self.var_radio = StringVar()
        radiobtn1 = Radiobutton(student_info_label, variable=self.var_radio, text="Take Photo Sample", value="Yes", bg="white")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = Radiobutton(student_info_label, variable=self.var_radio, text="No Photo Sample", value="No", bg="white")
        radiobtn2.grid(row=6, column=1)
        
        # button frame
        button_frame = Frame(student_info_label, bd=2, bg="white", relief="ridge")
        button_frame.place(x=0, y=255, width=715, height=38)

        # save button
        save_button = Button(button_frame, text="Save", command=self.add_data, width=11, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        save_button.grid(row=0, column=0, padx=1)

        # update button
        update_button = Button(button_frame, text="Update", command=self.update_data, width=12, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        update_button.grid(row=0, column=1, padx=1)

        # delete button
        delete_button = Button(button_frame, text="Delete", command=self.delete_data, width=11, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        delete_button.grid(row=0, column=2, padx=1)

        # reset button
        reset_button = Button(button_frame, text="Reset", width=12, command=self.reset_data, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        reset_button.grid(row=0, column=3, padx=1)

        # take photo button
        take_photo_button = Button(button_frame, text="Take Photo", command=self.generate_dataset, width=23, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        take_photo_button.grid(row=0, column=4, padx=1)

        # update photo button
        update_photo_button = Button(button_frame, text="Update Photo", width=23, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        update_photo_button.grid(row=0, column=5, padx=1)


        # Right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief="ridge", text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=730, height=580)

        # Right frame image
        img_right = Image.open("photo/istockphoto-1307457391-612x612.jpg")
        img_right = img_right.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        right_frame_img = Label(right_frame, image=self.photoimg_right)
        right_frame_img.place(x=5, y=0, width=720, height=120)

        # Search label
        search_label = LabelFrame(right_frame, text="Search Student Information", bg="white", relief="ridge", font=("times new roman", 12, "bold"))
        search_label.place(x=5, y=124, width=720, height=115)

        # Search by label
        search_by_label = Label(search_label, text="Search By", font=("times new roman", 12, "bold"), bg="white")
        search_by_label.grid(row=0, column=0, padx=10, sticky=W)

        # Search by combo
        search_by_combo = ttk.Combobox(search_label, font=("times new roman", 12, "bold"), state="readonly")
        search_by_combo["values"] = ("Select", "Roll No", "Phone No")
        search_by_combo.current(0)
        search_by_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Search entry
        search_entry = ttk.Entry(search_label, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        # Search button
        search_button = Button(search_label, text="Search", width=15, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        search_button.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        # showall button
        showall_button = Button(search_label, text="Show All", width=15, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        showall_button.grid(row=0, column=4, padx=1)

        #frame table
        table_frame = Frame(right_frame, bd=2, bg="white", relief="ridge")
        table_frame.place(x=5, y=240, width=720, height=315)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "class_div", "roll", "gender", "dob", "email", "phone", "address", "teacher_name","photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("class_div", text="Class Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher_name", text="Teacher Name")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("class_div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher_name", width=100)
        self.student_table.column("photo", width=100)


        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    #function declaration
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() =="" or self.var_id.get() == "" or self.var_roll.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn= mysql.connector.connect(host="localhost", username="root", password="12345678", database="face recognition system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),  
                                                                                                            self.var_class_div.get(),
                                                                                                            self.var_roll.get(),  
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher_name.get(),
                                                                                                            self.var_radio.get(),
                                                                                        
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #fetch data from database
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="face recognition system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    
    #get cursor
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_class_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher_name.set(data[13])
        self.var_radio.set(data[14])
    
    #update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() =="" or self.var_id.get() == "" or self.var_roll.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if update > 0:
                        conn= mysql.connector.connect(host="localhost", username="root", password="12345678", database="face recognition system")
                        my_cursor = conn.cursor()
                        my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photosample=%s where Student_ID=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_name.get(),  
                                                                                                                self.var_class_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher_name.get(),
                                                                                                                self.var_radio.get(),
                                                                                                                self.var_id.get()
                                                                                                                ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details have been updated successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student details?", parent=self.root)
                if delete > 0:
                    conn= mysql.connector.connect(host="localhost", username="root", password="12345678", database="face recognition system")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_ID=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student details have been deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")  
        self.var_class_div.set("Select Class Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher_name.set("")
        self.var_radio.set("")

    
    # generate dataset or take photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() =="" or self.var_id.get() == "" or self.var_roll.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn= mysql.connector.connect(host="localhost", username="root", password="12345678", database="face recognition system")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photosample=%s where Student_ID=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_name.get(),  
                                                                                                                self.var_class_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher_name.get(),
                                                                                                                self.var_radio.get(),
                                                                                                                self.var_id.get()==str(id+1)
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data on face frontals from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        img_cropped = img[y:y+h, x:x+w]
                        return img_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                        
                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed", parent=self.root)  
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)  

               

if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()