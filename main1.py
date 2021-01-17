from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox

from view import *
from ViewBooks import *
from adminpsd import *
# Add your own database name and password here to reflect in the code

root2 = Tk()
root2.title("Lib")
root2.minsize(width=400,height=400)
root2.geometry("600x500")

# Take n greater than 0.25 and less than 5
Canvas1 = Canvas(root2)


Canvas1.config(bg="black")
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root2,bg="red",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to\nTU Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


btn1 = Button(root2,text="Admin",bg='blue', fg='white', command=admin_psd)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    

btn2 = Button(root2,text="Student",bg='blue', fg='white', command=view_std_main)
btn2.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root2,text="VIew Books",bg='blue', fg='white', command=View)
btn2.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
    

root2.mainloop()
