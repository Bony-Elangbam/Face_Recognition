import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition 
from attendance import Attendance
from developer import Developer
from help import Help


# for windows === import os ===
# Replace this line:
# os.startfile("data")
# With the following line:
# subprocess.call(["open", "data"])



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # 1st img
        img1 = Image.open("college_images/BestFacialRecognition.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # 2nd img
        img2 = Image.open("college_images/facialrecognition.png")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # 3rd img
        img3 = Image.open("college_images/images.jpg")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # background img
        img4 = Image.open("college_images/ai_im2.webp")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0, y=0,width=1530,height=45)

        # ======= current time ======
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl = Label(title_lbl,font=("times new roman", 14,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # student button
        img5 = Image.open("college_images/student.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)

        # Detect Face button
        img6 = Image.open("college_images/face_detector1.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman", 15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=500,y=300,width=220,height=40)

        # Attendance face button
        img7 = Image.open("college_images/report.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman", 15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=800,y=300,width=220,height=40)

        # Help face button
        img8 = Image.open("college_images/help.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk ",cursor="hand2",command=self.help_data,font=("times new roman", 15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=1100,y=300,width=220,height=40)

        # Train face button
        img9 = Image.open("college_images/Train.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman", 15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=200,y=580,width=220,height=40)

        # Photos face button
        img10 = Image.open("college_images/photo.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=500,y=580,width=220,height=40)

        # Developer face button
        img11 = Image.open("college_images/Software-Development.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman", 15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=800,y=580,width=220,height=40)

        # Exit face button
        img12 = Image.open("college_images/exit.jpg")
        img12 = img12.resize((220, 220), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.exit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman", 15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=1100,y=580,width=220,height=40)
        

    # =========== Photo Buttons =======
    def open_img(self):
        subprocess.call(["open", "data"])

    # =========== Exit Buttons =======
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return

     # =============== Student Buttons =========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    # ======= Train  Model Button =====
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    # ======= Face Recognition Button =====
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    # ======= Face Recognition Button =====
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    # ======= Developer Button =====
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    # ======= Help Button =====
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


# ====errror=== 
#    clf=cv2.face.LBPHFaceRecognizer_create()  # Use correct module path
#      AttributeError: module 'cv2' has no attribute 'face_LBPHFaceRecognizer'
#   way to fix :
#        pip3 uninstall opencv-contrib-python3
#        pip3 install opencv-contrib-python3