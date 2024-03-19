from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import subprocess
import os
import numpy as np
from PIL import Image

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root,text="TRAIN DATA SET", font=("times new roman", 35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0, y=0,width=1530,height=45)

        img_top = Image.open("college_images/facialrecognition.png")
        img_top = img_top.resize((1530,325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        # ===== button===
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman", 30,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=0,y=380,width=1530,height=60)

        # =============

        img_bottom = Image.open("college_images/photo.jpg")
        img_bottom = img_bottom.resize((1530,325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if not file.startswith('.DS_Store')]

        faces = []
        ids = []

        for image_path in path:
            img = Image.open(image_path).convert('L')  # Convert image to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image_path)[1].split('.')[1]) # Extract the unique identifier from the filename

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)

        # Train the classifier And save
        clf=cv2.face.LBPHFaceRecognizer_create()  # Use correct module path
        clf.train(faces, ids)
        clf.write("classifier.xml")  # Write The Classifier
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Classifier Trained Successfully!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()