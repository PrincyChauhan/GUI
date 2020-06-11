#===============GRID LAYOUT===============

from tkinter import*
root=Tk()

lable1=Label(root,text="Name")
lable2=Label(root,text="Password")


entry1=Entry(root)
entry2=Entry(root)

lable1.grid(row=0)
lable2.grid(row=1)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

c=Checkbutton(root,text="Keep me logged in!!")
c.grid(columnspan=2)

root.mainloop()


# # =======Binding function layout========

# def printName(event):
#     print("Hello,I am Princy Chauhan")

# button1=Button(root,text=("Print my name"))

# button1.bind("<Button>",printName)
    
# button1.pack()

# root.mainloop()

