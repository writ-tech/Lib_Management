from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from AddStudent import *
from removeStudent import *


def mainc():
    
    
    mypass = "Sql!@#$1234"
    mydatabase="testdb"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("800x700")

    # Take n greater than 0.25 and less than 5
    same=True
    n=0.25

    # Adding a background image
    background_image =Image.open("lib.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    
     
        
   
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    headingFrame1 = Frame(root,bg="green",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.12)

    headingLabel = Label(headingFrame1, text="Admin Page", bg='black', fg='white', font=('Courier',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


 
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
    btn1 = Button(root,text="Add Book ",bg='black', fg='white', command=addBook)
    btn1.place(relx=0.28,rely=0.2, relwidth=0.45,relheight=0.1)
        
    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
    btn2.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root,text="View Books",bg='black', fg='white', command=View)
    btn3.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        
    btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
    btn4.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
    btn5.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    btn6 = Button(root,text="Add Student",bg='black', fg='white', command = addStudent)
    btn6.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    btn7 = Button(root,text="Remove Student",bg='black', fg='white', command = deletestd)
    btn7.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)



    root.mainloop()
   
