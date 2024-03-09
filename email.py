from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import os

class send_email:
    def __init__(self,root):
        self.root=root
        self.root.title("Send Mail Application")
        self.root.geometry('1000x700+200+50')
        self.root.resizable(False,False)
        self.root.config(bg="white") 

        self.email_icon=ImageTk.PhotoImage(file="C:\\Users\\Ajinkya\\Desktop\\face_recognition system\\college_image\\mail.png")
        title=Label(self.root,text="SEND YOUR EMAIL",image=self.email_icon,padx=10,compound=LEFT,font=("times new roman",48,"bold"),bg="black",fg="white",anchor="w").place(x=0,y=0,relwidth=1)

        to=Label(self.root,text="To(Email Address)",font=("times new roman",18,),bg="white").place(x=50,y=270)
        subj=Label(self.root,text="SUBJECT",font=("times new roman",18,),bg="white").place(x=50,y=330)
        msg=Label(self.root,text="MESSAGE",font=("times new roman",18,),bg="white").place(x=50,y=390)
        

        self.txt_to=Entry(self.root,font=("times new roman",14),bg="lightyellow")
        self.txt_to.place(x=300,y=275,width=350,height=30)
        self.txt_sub=Entry(self.root,font=("times new roman",14),bg="lightyellow")
        self.txt_sub.place(x=300,y=335,width=350,height=30)
        self.txt_msg=Text(self.root,font=("times new roman",12),bg="lightyellow")
        self.txt_msg.place(x=300,y=385,width=650,height=100)

        btn_send=Button(self.root,text="SEND",command=self.send_email,font=("times new roman",18,"bold"),bg="red",fg="black",cursor="hand2").place(x=700,y=530,width=120,height=30)
        btn_clear=Button(self.root,text="CLEAR",command=self.clear1,font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand2").place(x=830,y=530,width=120,height=30)
        btn_setting=Button(self.root,text="Setting",command=self.setting_window,font=("times new roman",18,"bold"),bg="lightblue",fg="black",cursor="hand2").place(x=870,y=233,width=120,height=30)

    def send_email(self):
        x=len(self.txt_msg.get('1.0',END))
        if self.txt_to.get()=="" or self.txt_sub.get()=="" or x==1:
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            messagebox.showinfo("Success","Email has been send")
    def clear1(self):
        self.txt_to.delete(0,END)
        self.txt_sub.delete(0,END)
        self.txt_msg.delete('1.0',END)

    def setting_window(self):
        self.root2=Toplevel()
        self.root2.title("setting")
        self.root2.geometry("700x450+350+90")
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.config(bg="white")

        title2=Label(self.root2,text="Credentials Setting",padx=10,compound=LEFT,font=("times new roman",48,"bold"),bg="black",fg="white",anchor="w").place(x=0,y=0,relwidth=1)
        desc=Label(self.root2,text="Enter the Email and Password from which to send the Email",padx=10,compound=LEFT,font=("times new roman",14),bg="green",fg="darkblue").place(x=0,y=90,relwidth=1)

        from_=Label(self.root2,text="Email Address",font=("times new roman",18,),bg="white").place(x=50,y=180)
        pass_=Label(self.root2,text="Password",font=("times new roman",18,),bg="white").place(x=50,y=250)

        self.txt_from=Entry(self.root2,font=("times new roman",14),bg="lightyellow")
        self.txt_from.place(x=250,y=180,width=300,height=30)
        self.txt_pass=Entry(self.root2,font=("times new roman",14),bg="lightyellow",show="*")
        self.txt_pass.place(x=250,y=250,width=300,height=30)

        
        btn_save=Button(self.root2,text="SAVE",command=self.save_setting,font=("times new roman",18,"bold"),bg="red",fg="black",cursor="hand2").place(x=200,y=330,width=120,height=30)
        
        btn_clear=Button(self.root2,text="CLEAR",command=self.clear2,font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand2").place(x=330,y=330,width=120,height=30)

    def save_setting(self):
        if self.txt_from.get()=="" or self.txt_pass.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            f=open('impoertant.txt','w')
            f.write(self.txt_from.get()+","+self.txt_pass.get())
            f.close() 
            messagebox.showinfo("Success","Save successfully",parent=self.root2)

    def clear2(self):
        self.txt_from.delete(0,END)
        self.txt_pass.delete(0,END)



if __name__== "__main__":
    root=Tk()
    obj=send_email(root)
    root.mainloop()