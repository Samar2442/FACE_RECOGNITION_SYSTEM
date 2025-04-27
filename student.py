from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import StringVar,Label,LabelFrame,Frame,W,Button,Radiobutton,HORIZONTAL,VERTICAL,RIGHT,BOTTOM,X,Y,END
import cv2
import logging
import os
import sys
from language import set_language, get_text  # Import language functions


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
        self.title_lbl = Label(bg_img, text=get_text("student_management_system"), font=("times new roman", 30, "bold"), bg="white", fg="blue")
        self.title_lbl.place(x=0, y=0, width=1530, height=45)

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
        self.current_course_label = LabelFrame(left_frame, text=get_text("current_course_information"), bg="white", relief="ridge", font=("times new roman", 12, "bold"))
        self.current_course_label.place(x=5, y=124, width=720, height=115)
        #department label
        self.dep_label = Label(self.current_course_label, text=get_text("department"), font=("times new roman", 12, "bold"), bg="white")
        self.dep_label.grid(row=0, column=0, padx=10, sticky=W)

        self.dep_combo = ttk.Combobox(self.current_course_label, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        self.dep_combo["values"] = (get_text("select_department"),
            get_text("cse"),
            get_text("it"),
            get_text("me"),
            get_text("ce"),
            get_text("ece"),
            get_text("ee"))
        self.dep_combo.current(0)
        self.dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course label
    
        self.course_label = Label(self.current_course_label, text=get_text("Course"), font=("times new roman", 12, "bold"), bg="white")
        self.course_label.grid(row=0, column=2, padx=10, sticky=W)

        self.course_combo = ttk.Combobox(self.current_course_label, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly")
        self.course_combo["values"] = (get_text("select_course"), get_text("B.E"), get_text("B.Tech"), get_text("M.E"), get_text("M.Tech"))
        self.course_combo.current(0)
        self.course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)


        # Year label
        self.year_label = Label(self.current_course_label, text=get_text("year"), font=("times new roman", 12, "bold"), bg="white")
        self.year_label.grid(row=1, column=0, padx=10, sticky=W)
        
        self.year_combo = ttk.Combobox(self.current_course_label, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly")
        self.year_combo["values"] = (get_text("select_year"), get_text("1st_year"), get_text("2nd_year"), get_text("3rd_year"), get_text("4th_year"))
        self.year_combo.current(0)
        self.year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester label
        self.semester_label = Label(self.current_course_label, text=get_text("semester"), font=("times new roman", 12, "bold"), bg="white")
        self.semester_label.grid(row=1, column=2, padx=10, sticky=W)

        self.semester_combo = ttk.Combobox(self.current_course_label, textvariable=self.var_sem, font=("times new roman", 12, "bold"), state="readonly")
        self.semester_combo["values"] = (get_text("select_semester"),get_text("1st_semester"), get_text("2nd_semester"), get_text("3rd_semester"),get_text("4th_semester"))
        self.semester_combo.current(0)
        self.semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        

        # Student information label
        self.student_info_label = LabelFrame(left_frame, text=get_text("student_information"), bg="white", relief="ridge", font=("times new roman", 12, "bold"))
        self.student_info_label.place(x=5, y=240, width=720, height=315)

        # Student ID label
        self.student_id_label = Label(self.student_info_label, text=get_text("student_id"), font=("times new roman", 12, "bold"), bg="white")
        self.student_id_label.grid(row=0, column=0, padx=10, sticky=W)

        self.student_id_entry = ttk.Entry(self.student_info_label, textvariable=self.var_id, font=("times new roman", 12, "bold"))
        self.student_id_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Student name label
        self.student_name_label = Label(self.student_info_label, text=get_text("student_name"), font=("times new roman", 12, "bold"), bg="white")
        self.student_name_label.grid(row=0, column=2, padx=10, sticky=W)

        self.student_name_entry = ttk.Entry(self.student_info_label, textvariable=self.var_name, font=("times new roman", 12, "bold"))
        self.student_name_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # class devision label
        self.class_div_label = Label(self.student_info_label, text=get_text("class_division"), font=("times new roman", 12, "bold"), bg="white")
        self.class_div_label.grid(row=1, column=0, padx=10, sticky=W)

        self.class_div_combo = ttk.Combobox(self.student_info_label, textvariable=self.var_class_div, font=("times new roman", 12, "bold"), state="readonly", width=18)
        self.class_div_combo["values"] = (get_text("select_class_division"), get_text("A"), get_text("B"), get_text("C"), get_text("D"))
        self.class_div_combo.current(0)
        self.class_div_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Roll no label
        self.roll_no_label = Label(self.student_info_label, text=get_text("roll_no"), font=("times new roman", 12, "bold"), bg="white")
        self.roll_no_label.grid(row=1, column=2, padx=10, sticky=W)

        self.roll_no_entry = ttk.Entry(self.student_info_label, textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        self.roll_no_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #gender label
        self.gender_label = Label(self.student_info_label, text=get_text("gender"), font=("times new roman", 12, "bold"), bg="white")
        self.gender_label.grid(row=2, column=0, padx=10, sticky=W)

        self.gender_combo = ttk.Combobox(self.student_info_label, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=18)
        self.gender_combo["values"] = (get_text("select_gender"),get_text("male"),get_text("female"),get_text("other"))
        self.gender_combo.current(0)
        self.gender_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        #dob label
        self.dob_label = Label(self.student_info_label, text=get_text("date_of_birth"), font=("times new roman", 12, "bold"), bg="white")
        self.dob_label.grid(row=2, column=2, padx=10, sticky=W)

        self.dob_entry = ttk.Entry(self.student_info_label, textvariable=self.var_dob, font=("times new roman", 12, "bold"))
        self.dob_entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # email label
        self.email_label = Label(self.student_info_label, text=get_text("email"), font=("times new roman", 12, "bold"), bg="white")
        self.email_label.grid(row=3, column=0, padx=10, sticky=W)

        self.email_entry = ttk.Entry(self.student_info_label, textvariable=self.var_email, font=("times new roman", 12, "bold"))
        self.email_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        # phone label
        self.phone_label = Label(self.student_info_label, text=get_text("phone_no"), font=("times new roman", 12, "bold"), bg="white")
        self.phone_label.grid(row=3, column=2, padx=10, sticky=W)

        self.phone_entry = ttk.Entry(self.student_info_label, textvariable=self.var_phone, font=("times new roman", 12, "bold"))
        self.phone_entry.grid(row=3, column=3, padx=2, pady=10, sticky=W)

        # address label
        self.address_label = Label(self.student_info_label, text=get_text("address"), font=("times new roman", 12, "bold"), bg="white")
        self.address_label.grid(row=4, column=0, padx=10, sticky=W)

        self.address_entry = ttk.Entry(self.student_info_label, textvariable=self.var_address, font=("times new roman", 12, "bold"))
        self.address_entry.grid(row=4, column=1, padx=2, pady=10, sticky=W)

        # teacher name label
        self.teacher_name_label = Label(self.student_info_label, text=get_text("teacher_name"), font=("times new roman", 12, "bold"), bg="white")
        self.teacher_name_label.grid(row=4, column=2, padx=10, sticky=W)

        self.teacher_name_entry = ttk.Entry(self.student_info_label, textvariable=self.var_teacher_name, font=("times new roman", 12, "bold"))
        self.teacher_name_entry.grid(row=4, column=3, padx=2, pady=10, sticky=W)

        #radio button
        self.var_radio = StringVar()
        self.radiobtn1 = Radiobutton(self.student_info_label, variable=self.var_radio, text=get_text("take_photo_sample"), value="Yes", bg="white")
        self.radiobtn1.grid(row=6, column=0)

        self.radiobtn2 = Radiobutton(self.student_info_label, variable=self.var_radio, text=get_text("no_photo_sample"), value="No", bg="white")
        self.radiobtn2.grid(row=6, column=1)
        
        # button frame
        button_frame = Frame(self.student_info_label, bd=2, bg="white", relief="ridge")
        button_frame.place(x=0, y=255, width=715, height=38)

        # save button
        self.save_button = Button(button_frame, text=get_text("save"), command=self.add_data, width=11, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        self.save_button.grid(row=0, column=0, padx=1)

        # update button
        self.update_button = Button(button_frame, text=get_text("update"), command=self.update_data, width=12, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        self.update_button.grid(row=0, column=1, padx=1)

        # delete button
        self.delete_button = Button(button_frame, text=get_text("delete"), command=self.delete_data, width=11, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        self.delete_button.grid(row=0, column=2, padx=1)

        # reset button
        self.reset_button = Button(button_frame, text=get_text("reset"), width=12, command=self.reset_data, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        self.reset_button.grid(row=0, column=3, padx=1)

        # take photo button
        self.take_photo_button = Button(button_frame, text=get_text("take_photo"), command=self.generate_dataset, width=23, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        self.take_photo_button.grid(row=0, column=4, padx=1)

        # update photo button
        self.update_photo_button = Button(button_frame, text=get_text("update_photo"), width=23, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        self.update_photo_button.grid(row=0, column=5, padx=1)


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
        self.search_label = LabelFrame(right_frame, text=get_text("search_student_information"), bg="white", relief="ridge", font=("times new roman", 12, "bold"))
        self.search_label.place(x=5, y=124, width=720, height=115)

        # Search by label
        self.search_by_label = Label(self.search_label, text=get_text("search_by"), font=("times new roman", 12, "bold"), bg="white")
        self.search_by_label.grid(row=0, column=0, padx=10, sticky=W)

        # Search by combo
        self.search_by_combo = ttk.Combobox(self.search_label, font=("times new roman", 12, "bold"), state="readonly")
        self.search_by_combo["values"] = (get_text("select"), get_text("roll_no"), get_text("phone_no"))
        self.search_by_combo.current(0)
        self.search_by_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Search entry
        self.search_entry = ttk.Entry(self.search_label, font=("times new roman", 12, "bold"))
        self.search_entry.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        # Search button
        self.search_button = Button(self.search_label, text=get_text("search"), width=15, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        self.search_button.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        # showall button
        self.showall_button = Button(self.search_label, text=get_text("show_all"), width=15, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        self.showall_button.grid(row=0, column=4, padx=1)

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

    def change_language(self, event):
        selected_lang = self.language_combo.get()
        if selected_lang in self.language_map:
            set_language(self.language_map[selected_lang])
            self.update_texts()

    def update_texts(self):
        # Placeholder for actual text update logic
        self.title_lbl.config(text=get_text("student_management_system"))
        self.home_button.config(text=get_text("home"))
        self.current_course_label.config(text=get_text("current_course_information"))
        self.dep_label.config(text=get_text("department"))
        self.current_course_label.config(text=get_text("select_department"))
        self.dep_combo["values"] = (
            get_text("select_department"),
            get_text("cse"),
            get_text("it"),
            get_text("me"),
            get_text("ce"),
            get_text("ece"),
            get_text("ee")
        )
        self.course_label.config(text=get_text("Course"))
        self.course_combo["values"] = (get_text("select_course"), get_text("B.E"), get_text("B.Tech"), get_text("M.E"), get_text("M.Tech"))
        self.year_combo.config(text=get_text("Year"))
        self.year_combo["values"] = (get_text("select_year"), get_text("1st_year"), get_text("2nd_year"), get_text("3rd_year"), get_text("4th_year"))
        self.semester_label.config(text=get_text("Semester"))
        self.semester_combo["values"] = (get_text("select_semester"),get_text("1st Semester"), get_text("2nd Semester"), get_text("3rd Semester"),get_text("4th Semester"))
        self.student_info_label.config(text=get_text("student_information"))
        self.student_id_label.config(text=get_text("student_iD"))
        self.student_name_label.config(text=get_text("student_name"))
        self.class_div_label.config(text=get_text("class_division"))
        self.class_div_combo["values"] = (get_text("select_class_division"), get_text("A"), get_text("B"), get_text("C"), get_text("D"))
        self.roll_no_label.config(text=get_text("roll_no"))
        self.gender_label.config(text=get_text("gender"))
        self.gender_combo["values"] = (get_text("Select Gender"),get_text("Male"),get_text("Female"),get_text("Other"))
        self.dob_label.config(text=get_text("date_of_birth"))
        self.email_label.config(text=get_text("email"))
        self.phone_label.config(text=get_text("phone_no"))
        self.address_label.config(text=get_text("address"))
        self.teacher_name_label.config(text=get_text("teacher_name"))
        self.radiobtn1.config(text=get_text("take_photo_sample"))
        self.radiobtn2.config(text=get_text("no_photo_sample"))
        self.save_button.config(text=get_text("save"))
        self.update_button.config(text=get_text("update"))
        self.delete_button.config(text=get_text("delete"))
        self.reset_button.config(text=get_text("reset"))
        self.take_photo_button.config(text=get_text("take_photo"))
        self.update_photo_button.config(text=get_text("update_photo"))
        self.search_label.config(text=get_text("search_student_information"))
        self.search_by_label.config(text=get_text("search_by"))
        self.search_by_combo["values"] = (get_text("select"), get_text("roll_no"), get_text("phone_no"))
        self.search_button.config(text=get_text("search"))
        self.showall_button.config(text=get_text("show_all"))

















               

if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()
