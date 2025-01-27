from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class ChatBot:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("730x620+0+0")
        self.root.title("ChatBot")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg="powder blue",width=620)
        main_frame.pack()

        img_chat=Image.open("C:\\Users\\Ajinkya\Desktop\\face_recognition system\\college_image\\chat.jpg")
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='darkblue',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RIDGE,font=('arial',14,),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg="white",width=730)
        btn_frame.pack()

        label=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',14,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',14,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=2,padx=5,sticky=W)

        self.msg=''
        self.label=Label(btn_frame,text=self.msg,font=('arial',12,'bold'),fg='red',bg='white')
        self.label.grid(row=1,column=1,padx=5,sticky=W)
    
    def enter_func(self,event): 
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


    def send(self):
        send='\t\t\t'+'You:'+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='Please enter some input'
            self.label.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label.config(text=self.msg,fg='red')
         
        if (self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif (self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif (self.entry.get()=='How are you?'):
            self.text.insert(END,'\n\n'+'Bot: fine and you')

        elif (self.entry.get()=='fantastic'):
            self.text.insert(END,'\n\n'+'Bot: Nice To Hear') 

        elif (self.entry.get()=='Who created you?'):
            self.text.insert(END,'\n\n'+'Bot: Mr.Ajinkya Shama did using python')

        elif (self.entry.get()=='What is your name?'):
            self.text.insert(END,'\n\n'+'Bot: My name is Mr.Hacker:)')

        elif (self.entry.get()=='Can you speak marathi?'):
            self.text.insert(END,'\n\n'+'Bot: Im still learning it.....')

        elif (self.entry.get()=='What is python programming?'):
            self.text.insert(END,'\n\n'+'Bot: Python is a computer programming language often used to build websites and software,automate tasks, and conduct data analysis. Python is a general purpose language, meaning it can be used to create a variety of different programs.')

        elif (self.entry.get()=='What is machine learning?'):
            self.text.insert(END,'\n\n'+'Bot: Machine learning is a branch of artificial intelligence (AI) and computer science\nwhich focuses on the use of data and algorithms to imitate the way that humans learn,gradually improving its accuracy.')

        elif (self.entry.get()=='How does facial recognition work?'):
            self.text.insert(END,'\n\n'+'Bot: Facial recognition uses computer-generated filters to transform face images into numerical expressions\nthat can be compared to determine their similarity. These filters are usually generated by using deep learning which uses artificial neural networks to process data.')
        
        elif (self.entry.get()=='How does facial recognition work step by step?'):
            self.text.insert(END,'\n\n'+'Bot: Step 1: Face detection\nThe camera detects and locates the image of a face\nStep 2: Face analysis\nNext, an image of the face is captured and analyzed. Most facial recognition technology relies on 2D rather than 3D images because it can more conveniently match a 2D image with public photos or those in a database.\nStep 3: Converting the image to data\nThe face capture process transforms analog information (a face) into a set of digital information (data) based on the persons facial features.\nStep 4: Finding a match\n If your faceprint matches an image in a facial recognition database, then a determination is made.')        

        elif (self.entry.get()=='What is cahtbot?'):
            self.text.insert(END,'\n\n'+'Bot: A chatbot is a computer program that simulates and processes human conversation (either written or spoken),\nallowing humans to interact with digital devices as if they were communicating with a real person.')

        elif (self.entry.get()=='Bye'):
            self.text.insert(END,'\n\n'+'Bot: Thanku for Chatting:)')

        else:
            self.text.insert(END,'\n\n'+'Bot: Sorry i did not get it')

  
if __name__== "__main__":
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()
