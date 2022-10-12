from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

root = Tk()
root.title("registration page")
root.geometry('1800x900')

background=ImageTk.PhotoImage(Image.open("bg.jpg"))
imglbl=Label(root, image=background).pack()

namelbl=Label(root,text="Name",font="normal").place(x=450,y=200)
emaillbl=Label(root,text="Email",font="normal").place(x=450,y=250)
contactlbl=Label(root,text="Contact",font="normal").place(x=450,y=300)
addresslbl=Label(root,text="Address",font="normal").place(x=450,y=350)
passwordlbl=Label(root,text="Password",font="normal").place(x=450,y=400)
Repasswordlbl=Label(root,text="Re password",font="normal").place(x=450,y=450)

name=Entry(root, width=40, font="normal").place(x=650,y=200)
email=Entry(root, width=40, font="normal").place(x=650,y=250)
contact=Entry(root, width=40, font="normal").place(x=650,y=300)
address=Entry(root, width=40, font="normal").place(x=650,y=350)
password=Entry(root, width=40, font="normal").place(x=650,y=400)
repassword=Entry(root, width=40, font="normal",textvariable=password,show="*").place(x=650,y=450)

register=Button(root, text="Register", bg="white" ,height=1 , width=8,font="normal", command=root.quit, fg="green").place(x=700,y=500)



root.mainloop()