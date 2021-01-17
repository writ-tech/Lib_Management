from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code



    
def view_std():
    mypass = "Sql!@#$1234"
    mydatabase="testdb"
    ID=SID.get()
    PSD=password.get()

        
    print(ID)
    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

# Enter Table Names here
    studentTable="students"
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="blue",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-20s%-20s%-20s%-20s%-20s"%('Book1','Book2','Book3','Book4','Book5'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from "+studentTable+" where SID= '"+ID+"'"
    if PSD=="password":
        
        try:
            cur.execute(getBooks)
            con.commit()
            for i in cur:
                Label(labelFrame, text="%-20s%-30s%-30s%-20s%-30s"%(i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white').place(relx=0.07,rely=y)
                y += 0.1
                
        except:
            messagebox.showinfo("Failed to fetch files from database")
        
        quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
        quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
        
        root.mainloop()
    else :
         messagebox.showinfo("Wrong password")
         root.destroy()
    root.destroy()        
def view_std_main():
    global SID,password
    root1 = Tk()
    root1.title("Library")
    root1.minsize(width=400,height=400)
    root1.geometry("800x700")

        
    Canvas1 = Canvas(root1)
        
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root1,bg="green",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.12)

    headingLabel = Label(headingFrame1, text="Student Page", bg='black', fg='white', font=('Courier',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

            
    labelFrame = Frame(root1,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
            
        # Book ID to Delete
    lb2 = Label(labelFrame,text="Student ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
    
            
    SID = Entry(labelFrame)
    SID.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    lb3 = Label(labelFrame,text="Password : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.6)
    
    password = Entry(labelFrame)
    password.place(relx=0.3,rely=0.6, relwidth=0.62)        
        #Submit Button
    SubmitBtn = Button(root1,text="SUBMIT",bg='#d1ccc0', fg='black',command=view_std)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
        
    quitBtn = Button(root1,text="Quit",bg='#f7f1e3', fg='black', command=root1.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root1.mainloop()
    
    

