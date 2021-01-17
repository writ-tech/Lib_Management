

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from main2 import *
def verify():
    adminpsd=password.get()
    if adminpsd=="root":
        mainc()
        
        
    else:
        messagebox.showinfo("Wrong password")
        root1.destroy()
        
        
        
    root1.destroy()

 
def admin_psd():
    global password,root1
    root1 = Tk()
    root1.title("Library")
    root1.minsize(width=400,height=400)
    root1.geometry("800x700")

        
    Canvas1 = Canvas(root1)
        
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root1,bg="green",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.12)

    headingLabel = Label(headingFrame1, text="Admin Password", bg='black', fg='white', font=('Courier',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

            
    labelFrame = Frame(root1,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
            

    
    lb3 = Label(labelFrame,text="Password : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.6)
    
    password = Entry(labelFrame)
    password.place(relx=0.3,rely=0.6, relwidth=0.62)        
        #Submit Button
    SubmitBtn = Button(root1,text="SUBMIT",bg='#d1ccc0', fg='black',command=verify)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
        
    quitBtn = Button(root1,text="Quit",bg='#f7f1e3', fg='black', command=root1.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root1.mainloop()
    
