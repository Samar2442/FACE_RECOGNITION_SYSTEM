from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root): 
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

        # Title label       
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
        try:
            img_top = Image.open(r"photo\face-recognition-personal-identification-collage (3).jpg")
            img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            top_img_label = Label(self.root, image=self.photoimg_top)
            top_img_label.place(x=0, y=45, width=1530, height=325)
        except Exception as e:
            print("Top image load error:", e)

        # Train button
        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 30, "bold"), bg="blue", fg="white")
        b1_1.place(x=0, y=370, width=1530, height=70)

        # Bottom image
        try:
            img_bottom = Image.open(r"photo\istockphoto-1307457391-612x612.jpg")
            img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            bottom_img_label = Label(self.root, image=self.photoimg_bottom)
            bottom_img_label.place(x=0, y=440, width=1530, height=325)
        except Exception as e:
            print("Bottom image load error:", e)

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

if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()
