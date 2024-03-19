from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
from register import Register


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

        self.bg=ImageTk.PhotoImage(file="hotel_images/SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1 = Image.open("college_images/LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label( image=self.photoimg1,bg="black",borderwidth=0)
        f_lbl.place(x=730, y=175, width=100, height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=115,y=110)

        # label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=150)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=185,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=255,width=270)

        # ===Icone Image =====
        img2 = Image.open("college_images/LoginIconAppl.png")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label( image=self.photoimg2,bg="black",borderwidth=0)
        f_lbl.place(x=650, y=320, width=25, height=25)

        img3 = Image.open("college_images/lock-512.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label( image=self.photoimg3,bg="black",borderwidth=0)
        f_lbl.place(x=650, y=395, width=25, height=25)

        # ==login button==
        b1_1=Button(frame,text="Login",command=self.login,font=("times new roman", 15,"bold"),bd=3,relief=RIDGE,bg="red",fg="black",highlightbackground="red",activebackground="red",activeforeground="black")
        b1_1.place(x=110,y=300,width=120,height=35)

        # ===register button===
        b2_1=Button(frame,text="New User Register",command=self.register_window,font=("times new roman", 10,"bold"),borderwidth=0,bd=3,relief=RIDGE,bg="black",fg="black",activebackground="black",activeforeground="black")
        b2_1.place(x=15,y=350,width=160)

        # ===forgot password===
        b3_1=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman", 10,"bold"),borderwidth=0,bd=3,relief=RIDGE,bg="black",fg="black",activebackground="black",activeforeground="black")
        b3_1.place(x=15,y=380,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field are required")
        elif self.txtuser.get()=="bony" and self.txtpass.get()=="123":
                messagebox.showinfo("Success","Welcome to Face Recognition System")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Bony123@",database="logdata")
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                 messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("yesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()

    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")

    # ==== reset password ====
    def reset_pass(self):
        if self.securityQ_combo.get()=="Select":
            messagebox.showerror("Error","Select the security Question",parent=self.root2)
        elif self.txt_securityA.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_pass.get()=="":
            messagebox.showerror("Error","please enter the New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Bony123@",database="logdata")
            my_cursor=conn.cursor()
            qeury=("Select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.securityQ_combo.get(),self.txt_securityA.get())
            my_cursor.execute(qeury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please entere the Correct Answer",parent=self.root2)
            else:
                query=("Update register set password=%s where email=%s")
                value=(self.txt_new_pass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Please login with your new password",parent=self.root2)
                self.root2.destroy()


 # ===============forgot password ===============
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to rest password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Bony123@",database="logdata")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please entere the valid email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1,)

                securityQ=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
                securityQ.place(x=50,y=80)

                self.securityQ_combo=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly",width=30)
                self.securityQ_combo["values"]=("Select","Your Birth Place","Your Pet Name","Your School Name")
                self.securityQ_combo.current(0)
                self.securityQ_combo.place(x=50,y=110,width=250)

                securityA=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
                securityA.place(x=50,y=150)

                self.txt_securityA=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_securityA.place(x=50,y=180,width=250)

                new_pass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white")
                new_pass.place(x=50,y=220)

                self.txt_new_pass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_pass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="black",bg="white")
                btn.place(x=100,y=290)



#===== register part ======
# class Register:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Register")

#         # ====== variable ====
#         self.var_fname=StringVar()
#         self.var_lname=StringVar()
#         self.var_contact=StringVar()
#         self.var_email=StringVar()
#         self.var_securityQ=StringVar()
#         self.var_securityA=StringVar()
#         self.var_pass=StringVar()
#         self.var_confpass=StringVar()

        

#         self.bg=ImageTk.PhotoImage(file="hotel_images/back.jpg")
#         lbl_bg=Label(self.root,image=self.bg)
#         lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

#         self.bg1=ImageTk.PhotoImage(file="hotel_images/thought-good-morning-messages-LoveSove.jpg")
#         left_bg=Label(self.root,image=self.bg1)
#         left_bg.place(x=50,y=100,width=470,height=550)

#         frame=Frame(self.root,bg="white")
#         frame.place(x=520,y=100,width=800,height=550)

#         reg_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
#         reg_lbl.place(x=20,y=20)

#         # =====label and entry =====

#         # ===== row 1 =======
#         fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="white")
#         fname.place(x=50,y=100)

#         self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
#         self.txt_fname.place(x=50,y=130,width=250)

#         lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
#         lname.place(x=370,y=100)

#         self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
#         self.txt_lname.place(x=370,y=130,width=250)

#         # ===== row 2 =======
#         contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
#         contact.place(x=50,y=170)

#         self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
#         self.txt_contact.place(x=50,y=200,width=250)

#         email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
#         email.place(x=370,y=170)

#         self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
#         self.txt_email.place(x=370,y=200,width=250)

#         # ===== row 3 =======
#         securityQ=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
#         securityQ.place(x=50,y=240)

#         self.securityQ_combo=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly",width=30)
#         self.securityQ_combo["values"]=("Select","Your Birth Place","Your Pet Name","Your School Name")
#         self.securityQ_combo.current(0)
#         self.securityQ_combo.place(x=50,y=270,width=250)

#         securityA=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
#         securityA.place(x=370,y=240)

#         self.txt_securityA=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
#         self.txt_securityA.place(x=370,y=270,width=250)

#         # ===== row 4 =======
#         paswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
#         paswd.place(x=50,y=310)

#         self.txt_paswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
#         self.txt_paswd.place(x=50,y=340,width=250)

#         confirm_paswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
#         confirm_paswd.place(x=370,y=310)

#         self.txt_confirm_paswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
#         self.txt_confirm_paswd.place(x=370,y=340,width=250)

#         # ========== check button ====
#         self.var_check=IntVar()
#         checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0,bg="white")
#         checkbtn.place(x=60,y=380)

#         # ======= button ======
#         img1 = Image.open("college_images/register-now-button1.jpg")
#         img1 = img1.resize((200, 40), Image.LANCZOS)
#         self.photoimg1 = ImageTk.PhotoImage(img1)
#         b1=Button(frame,image=self.photoimg1,command=self.register_data,cursor="hand2",borderwidth=0,font=("times new roman",15,"bold"),fg="white")
#         b1.place(x=10,y=420,width=200)

#         img2 = Image.open("college_images/loginpng.png")
#         img2 = img2.resize((200, 40), Image.LANCZOS)
#         self.photoimg2 = ImageTk.PhotoImage(img2)
#         b2=Button(frame,image=self.photoimg2,command=self.return_login,cursor="hand2",borderwidth=0,font=("times new roman",15,"bold"),fg="white")
#         b2.place(x=330,y=420,width=200)

#         # ========== function decleration
#     def register_data(self):
#         if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
#             messagebox.showerror("Error","All fields are required")
#         elif self.var_pass.get()!=self.var_confpass.get():
#             messagebox.showerror("Error","Password & Confirm Password must be same")
#         elif self.var_check.get()==0:
#             messagebox.showerror("Error","Please agree our terms and condition")
#         else:
#             conn=mysql.connector.connect(host="localhost",username="root",password="Bony123@",database="logdata")
#             my_cursor=conn.cursor()
#             query=("Select * from register where email=%s")
#             value=(self.var_email.get(),)
#             my_cursor.execute(query,value)
#             row=my_cursor.fetchone()
#             if row!=None:
#                 messagebox.showerror("Error","User already exist, please try another email")
#             else:
#                 my_cursor.execute("Insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
#                                                                                     self.var_fname.get(),
#                                                                                     self.var_lname.get(),
#                                                                                     self.var_contact.get(),
#                                                                                     self.var_email.get(),
#                                                                                     self.var_securityQ.get(),
#                                                                                     self.var_securityA.get(),
#                                                                                     self.var_pass.get()
#                                                                                 ))
#                 conn.commit()
#                 conn.close()
#                 messagebox.showinfo("Success","Register Successfull")
#                 self.root.destroy()


#     def return_login(self):
#         self.root.destroy()

    
if __name__ == "__main__":
    main()