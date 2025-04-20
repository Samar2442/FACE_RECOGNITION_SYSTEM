from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import _mysql_connector
import os
import csv
from datetime import datetime
from time import strftime

mydata = []


class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

        # First image
        img = Image.open("photo/istockphoto-1430114131-612x612.jpg")
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Second image
        img1 = Image.open("photo/istockphoto-1307457391-612x612.jpg")
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg2)
        f_lbl1.place(x=800, y=0, width=800, height=200)

        # Background image
        img3 = Image.open("photo/GettyImages-1072191138.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=710)

        # Title label
        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        # Left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief="ridge", text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)

        # Left frame image
        img_left = Image.open("photo/GettyImages-1072191138.jpg")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        left_frame_img = Label(left_frame, image=self.photoimg_left)
        left_frame_img.place(x=5, y=0, width=720, height=120)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=300)

        # Labels and entries
        attendence_id_label = Label(left_inside_frame, text="STUDENT ID", font=("times new roman", 12, "bold"), bg="white")
        attendence_id_label.grid(row=0, column=0, padx=10, sticky=W)

        attendence_id_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"))
        attendence_id_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        studentName_label = Label(left_inside_frame, text="NAME", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=4, pady=8)

        studentName_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, pady=8)

        class_label = Label(left_inside_frame, text="SEMESTER", font=("times new roman", 12, "bold"), bg="white")
        class_label.grid(row=1, column=0)

        semester_combo = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "1st Semester", "2nd Semester", "3rd Semester", "4th Semester",
                                    "5th Semester", "6th Semester", "7th Semester", "8th Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=1, padx=2, pady=18)

        student_dept_label = Label(left_inside_frame, text="DEPARTMENT", font=("times new roman", 12, "bold"), bg="white")
        student_dept_label.grid(row=1, column=2)

        student_dept_combo = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), state="readonly")
        student_dept_combo["values"] = ("Select Department", "CSE", "IT", "ME", "CE", "ECE", "EE")
        student_dept_combo.current(0)
        student_dept_combo.grid(row=1, column=3, pady=8)

        current_date = datetime.now().strftime("%Y-%m-%d")
        self.date_var = StringVar(value=current_date)
        self.time_var = StringVar()
        self.update_time()

        Date_label = Label(left_inside_frame, text="DATE", font=("times new roman", 12, "bold"), bg="white")
        Date_label.grid(row=2, column=0)

        Date_entry = ttk.Entry(left_inside_frame, textvariable=self.date_var, font=("times new roman", 12, "bold"), state="readonly")
        Date_entry.grid(row=2, column=1, pady=8)

        time_label = Label(left_inside_frame, text="TIME", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=2)

        time_entry = ttk.Entry(left_inside_frame, textvariable=self.time_var, font=("times new roman", 12, "bold"), state="readonly")
        time_entry.grid(row=2, column=3, pady=8)

        attendence_id_label = Label(left_inside_frame, text="Student status", font=("times new roman", 12, "bold"), bg="white")
        attendence_id_label.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Buttons
        button_frame = Frame(left_inside_frame, bd=2, bg="white", relief="ridge")
        button_frame.place(x=0, y=255, width=715, height=38)

        save_button = Button(button_frame, text="Import csv", command=self.importCSV, width=11,
                             font=("times new roman", 9, "bold"), bg="blue", fg="white")
        save_button.grid(row=0, column=0, padx=1)

        update_button = Button(button_frame, text="Export csv", command=self.exportCSV, width=12,
                               font=("times new roman", 9, "bold"), bg="blue", fg="white")
        update_button.grid(row=0, column=1, padx=1)

        delete_button = Button(button_frame, text="Update", width=11, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        delete_button.grid(row=0, column=2, padx=1)

        reset_button = Button(button_frame, text="Reset", width=12, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        reset_button.grid(row=0, column=3, padx=1)

        # Right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief="ridge", text="Student Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=730, height=580)

        table_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,
                                                  column=("id", "roll", "name", "department", 'time', "date", "attendance"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading('id', text="ATTENDANCE ID")
        self.AttendanceReportTable.heading('roll', text="ROLL")
        self.AttendanceReportTable.heading('name', text="NAME")
        self.AttendanceReportTable.heading('department', text="DEPARTMENT")
        self.AttendanceReportTable.heading('time', text="TIME")
        self.AttendanceReportTable.heading('date', text="DATE")
        self.AttendanceReportTable.heading('attendance', text="ATTENDANCE")

        self.AttendanceReportTable['show'] = "headings"
        self.AttendanceReportTable.column("id", width=150)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=150)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCSV(self):
        try:
            fln = filedialog.askopenfilename(
              initialdir=os.getcwd(),
              title='Open CSV',
              filetypes=[('CSV File', '.csv'), ('All Files', '.*')],
              parent=self.root
        )
            if not fln:
              return
            with open(fln, mode='r', newline='') as myfile:
              csvread = csv.reader(myfile)
              mydata = []
              for index, row in enumerate(csvread):
                  if len(row) != 7:
                      continue
                  mydata.append(row)
                  self.fetchData(mydata)
            messagebox.showinfo("Data Imported", f"Data successfully imported from {os.path.basename(fln)}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"An error occurred while importing data:\n{str(es)}", parent=self.root)

    def exportCSV(self):
        try:
            if len(self.AttendanceReportTable.get_children()) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False

            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title='Save CSV',
                defaultextension=".csv",
                filetypes=[('CSV File', '.csv'), ('All Files', '.*')],
                parent=self.root
            )
            if not fln:
                return

            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile)
                for row_id in self.AttendanceReportTable.get_children():
                    row = self.AttendanceReportTable.item(row_id)['values']
                    exp_write.writerow(row)
            messagebox.showinfo("Data Exported", f"Your data was successfully exported to {os.path.basename(fln)}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"An error occurred while exporting data:\n{str(es)}", parent=self.root)

    def update_time(self):
        current_time = strftime('%H:%M:%S %p')
        self.time_var.set(current_time)
        self.root.after(1000, self.update_time)


# Main Entry Point
if __name__ == "__main__":
    root = Tk()
    app = Attendence(root)
    root.mainloop()
