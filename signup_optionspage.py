from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title(" sign up ")
root.geometry("595x500")

background=ImageTk.PhotoImage(Image.open("loginimg.jpg"))
imglbl=Label(root, image=background).pack()

lbl=Label(root,text=" SIGN UP " ,bg="red", fg="white",font="normal" ,padx=260 ,pady=10 ).place(x=0,y=50)


button1=Button(root,text="Customer",font="normal",width=8,height=2,fg="green",bg="white").place(x=150,y=200)
button2=Button(root,text="Driver",font="normal",width=8,height=2,fg="green",bg="white").place(x=350,y=200)
button3=Button(root,text="admin",font="normal",width=8,height=2,fg="green",bg="white").place(x=250,y=270)


root.mainloop()
