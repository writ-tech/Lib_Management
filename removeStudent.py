from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "Sql!@#$1234"
mydatabase="testdb"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()



def deleteStudent():
    
    sid = std_id.get()
    
    deleteSql = "delete from students where SID = '"+sid+"'"
    find= " select * from students where SID ='"+sid+"'"
    cur.execute(find)
    con.commit()
    b=0
    for i in cur:
      for j in range(1,6):
          print(i[j])
          if i[j]!='N':
             b=1
             break
    if b==1:
        messagebox.showinfo('Error',"Can't delete as student hasn't returned a book")
    else :    

        try:
            cur.execute(deleteSql)
            con.commit()
            
            messagebox.showinfo('Success',"Student Record Deleted Successfully")
        except:
            messagebox.showinfo("Please check Student ID")
    

    

    
    root.destroy()
    
def deletestd(): 
    
    global std_id,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="brown",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Student_Removal", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Student ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    std_id = Entry(labelFrame)
    std_id.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteStudent)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
