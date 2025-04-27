
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import logging
import os
import sys
from language import set_language, get_text  # Import language functions


class Train:
    def __init__(self, root): 
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

        # Title label       
        title_lbl = Label(self.root, text=get_text("train_data_set"), font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=100)

        # Home button
        img = Image.open(r"photo/beautiful-home_24877-50819.jpg")
        img = img.resize((70, 70), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        b1 = Button(title_lbl, image=self.photoimg, command=self.go_to_home, cursor="hand2")
        b1.place(x=10, y=0, width=70, height=70)

        self.home_button = Button(title_lbl, text=get_text("home"), command=self.go_to_home, cursor="hand2", font=("times new roman", 13, "bold"), bg="lavender", fg="black")
        self.home_button.place(x=10, y=70, width=70, height=30)

        # Top image
        try:
            img_top = Image.open(r"photo\face-recognition-personal-identification-collage (3).jpg")
            img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            top_img_label = Label(self.root, image=self.photoimg_top)
            top_img_label.place(x=0, y=100, width=1530, height=325)
        except Exception as e:
            print("Top image load error:", e)

        # Train button
        self.b1_1 = Button(self.root, text=get_text("train_data"), command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 30, "bold"), bg="blue", fg="white")
        self.b1_1.place(x=0, y=370, width=1530, height=70)

        # Bottom image
        try:
            img_bottom = Image.open(r"photo\istockphoto-1307457391-612x612.jpg")
            img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            bottom_img_label = Label(self.root, image=self.photoimg_bottom)
            bottom_img_label.place(x=0, y=440, width=1530, height=325)
        except Exception as e:
            print("Bottom image load error:", e)

    def go_to_home(self):
        """This method will close the current Developer window and open the main application window."""
        self.root.destroy()  # Close the current Developer window
        self.open_main_window()  # Open the main application window

    def open_main_window(self):
        """Opens the main window (main.py)"""
        try:
            import main  # Import your main window module here
            # Assuming `main.py` has a `Face_Recognition_System()` function to start the app
            main.Face_Recognition_System()
        except ImportError:
            logging.error("Error importing the main window module. Ensure 'main.py' exists.")

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data directory '{data_dir}' not found.")
            return

        image_paths = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.png', '.jpeg'))]

        faces = []
        ids = []

        for image_path in image_paths:
            try:
                img = Image.open(image_path).convert('L')  # Grayscale
                image_np = np.array(img, 'uint8')
                id = int(os.path.split(image_path)[1].split('.')[1])
                faces.append(image_np)
                ids.append(id)
                cv2.imshow("Training", image_np)
                cv2.waitKey(1)
            except Exception as e:
                print(f"Error processing {image_path}: {e}")

        if not faces:
            messagebox.showwarning("Warning", "No valid images found for training.")
            return

        ids = np.array(ids)

        # Train the classifier and save it
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed successfully.")

    def change_language(self, event):
        selected_lang = self.language_combo.get()
        if selected_lang in self.language_map:
            set_language(self.language_map[selected_lang])
            self.update_texts()

    def update_texts(self):
        # Placeholder for actual text update logic
        self.title_lbl.config(text=get_text("train_data_set"))
        self.home_button.config(text=get_text("home"))
        self.b1_1.config(text=get_text("train_data"))

logging.basicConfig(level=logging.INFO)   

if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()
