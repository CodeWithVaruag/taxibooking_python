from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image


import password as password

root = Tk()
root.title("login Page")
root.geometry('')


background=ImageTk.PhotoImage(Image.open("log.png"))
imglbl=Label(root, image=background).pack()
# the label for user_name
email_lbl = Label(root, text="E-mail",font="normal").place(x=600, y=250)

# the label for user_password
password_lbl = Label(root, text="Password", font="normal").place(x=600, y=310)

login_button = Button(root, text="Login", bg="white" ,height=1 , width=8, font="normal", command=root.quit, fg="red").place(x=700, y=400)

email_input_area = Entry(root, width=40, font="normal").place(x=740, y=255)

user_password_entry_area = Entry(root, width=40, font="normal", textvariable=password, show="*").place(x=740, y=315)

register_btn=Button(root, text="sign up", bg="white" ,height=1 , width=8,font="normal", command=root.quit, fg="green").place(x=850,y=400)

root.mainloop()

# adding button to the frame

# img = PhotoImage(file="loginimg.jpg")
# backgroundlabel = Label(image="img")
# backgroundlabel.pack()



