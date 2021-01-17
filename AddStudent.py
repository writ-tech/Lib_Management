from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def studentRegister():
    
    sid =std_ID.get()
    name =std_name.get()

    
    insertstudent= "insert into students (SID,name) values('"+sid+"','"+name+"')"
    try:
        cur.execute(insertstudent)
        con.commit()
        messagebox.showinfo('Success',"Student added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    



    root.destroy()
    
def addStudent(): 
    
    global std_name,std_ID,studentTable,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "Sql!@#$1234"
    mydatabase="testdb"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    studentTable = "students" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="brown",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Student_Addition", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Student_name : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    std_name= Entry(labelFrame)
    std_name.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Student_ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    std_ID = Entry(labelFrame)
    std_ID.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
   
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=studentRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
