from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register")

        # ====== variable ====
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        

        self.bg=ImageTk.PhotoImage(file="hotel_images/back.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file="hotel_images/thought-good-morning-messages-LoveSove.jpg")
        left_bg=Label(self.root,image=self.bg1)
        left_bg.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        reg_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        reg_lbl.place(x=20,y=20)

        # =====label and entry =====

        # ===== row 1 =======
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txt_fname.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        # ===== row 2 =======
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        # ===== row 3 =======
        securityQ=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
        securityQ.place(x=50,y=240)

        self.securityQ_combo=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly",width=30)
        self.securityQ_combo["values"]=("Select","Your Birth Place","Your Pet Name","Your School Name")
        self.securityQ_combo.current(0)
        self.securityQ_combo.place(x=50,y=270,width=250)

        securityA=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
        securityA.place(x=370,y=240)

        self.txt_securityA=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_securityA.place(x=370,y=270,width=250)

        # ===== row 4 =======
        paswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        paswd.place(x=50,y=310)

        self.txt_paswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_paswd.place(x=50,y=340,width=250)

        confirm_paswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        confirm_paswd.place(x=370,y=310)

        self.txt_confirm_paswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_paswd.place(x=370,y=340,width=250)

        # ========== check button ====
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0,bg="white")
        checkbtn.place(x=60,y=380)

        # ======= button ======
        img1 = Image.open("college_images/register-now-button1.jpg")
        img1 = img1.resize((200, 40), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimg1,command=self.register_data,cursor="hand2",borderwidth=0,font=("times new roman",15,"bold"),fg="white")
        b1.place(x=10,y=420,width=200)

        img2 = Image.open("college_images/loginpng.png")
        img2 = img2.resize((200, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2=Button(frame,image=self.photoimg2,cursor="hand2",borderwidth=0,font=("times new roman",15,"bold"),fg="white")
        b2.place(x=330,y=420,width=200)

        # ========== function decleration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Bony123@",database="")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("Insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()
                                                                                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfull")

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()