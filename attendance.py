from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        # ===== variable ===
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # 1st img
        img1 = Image.open("college_images/smart-attendance.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # 2nd img
        img2 = Image.open("college_images/iStock-182059956_18390_t12.jpg")
        img2 = img2.resize((800, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # bg img
        img3 = Image.open("college_images/wp2551980.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0, y=0,width=1530,height=45)

        # frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1480,height=600)

        # left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open("college_images/AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720,130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=725,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=720,height=370)


        # Label and entry
        # attendance id
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # roll
        roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        roll_entry.grid(row=0,column=3,pady=8,sticky=W)

        # name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        name_label.grid(row=1,column=0)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=1,column=1,pady=8)

        # department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=1,column=2)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        dep_entry.grid(row=1,column=3,pady=8)

        # time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=2,column=0)

        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,pady=8)

        # date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        date_label.grid(row=2,column=2)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,pady=8)

        # attendance
        attend_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")
        attend_label.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",13,"bold"),state="readonly",width=20)
        self.atten_status["values"]=("Select Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,pady=8)

        # buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=20,font=("times new roman",13,"bold"),bg="blue",fg="Black")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=20,font=("times new roman",13,"bold"),bg="blue",fg="Black")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=20,font=("times new roman",13,"bold"),bg="blue",fg="Black")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",13,"bold"),bg="blue",fg="Black")
        reset_btn.grid(row=0,column=3)

        # right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        # ==== sroll bar table =======
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attend_table=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attend_table.xview)
        scroll_y.config(command=self.attend_table.yview)

        self.attend_table.heading("id",text="Attendance ID")
        self.attend_table.heading("roll",text="Roll")
        self.attend_table.heading("name",text="Name")
        self.attend_table.heading("department",text="Department")
        self.attend_table.heading("time",text="Time")
        self.attend_table.heading("date",text="Date")
        self.attend_table.heading("attendance",text="Attendance")

        self.attend_table["show"]="headings"

        self.attend_table.column("id",width=100)
        self.attend_table.column("roll",width=100)
        self.attend_table.column("name",width=100)
        self.attend_table.column("department",width=100)
        self.attend_table.column("time",width=100)
        self.attend_table.column("date",width=100)
        self.attend_table.column("attendance",width=100)

        self.attend_table.pack(fill=BOTH,expand=1)

        self.attend_table.bind("<ButtonRelease>",self.get_cursor)


    # ========= fetch data =======
    def fetchData(self,rows):
        self.attend_table.delete(*self.attend_table.get_children())
        for i in rows:
            self.attend_table.insert("",END,values=i)

    # ===== import csv ====
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("csv File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # ====== export csv ===
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("csv File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.attend_table.focus()
        content=self.attend_table.item(cursor_row)
        rows=content['values']

        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
            self.var_atten_id.set("")
            self.var_atten_roll.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()