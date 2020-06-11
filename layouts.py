from tkinter import*
root=Tk()
topFrame=Frame(root)
topFrame.pack()

# bottomFrame=Frame(root)
# bottomFrame.pack(side=BOTTOM)

button1=Button(topFrame,text="Button1",fg="red")
# button1.pack()
button1.pack(side=LEFT)


button2=Button(topFrame,text="Button2",fg="red")
button2.pack(side=LEFT)


button3=Button(topFrame,text="Button3",fg="red")
button3.pack(side=LEFT)

button4=Button(topFrame,text="Button4",fg="red")
button4.pack(side=LEFT)


root.mainloop()

# =====================Fitting Widgets in layout========================

# one=Label(root,text="one",bg="red",fg="white")
# one.pack()

# two=Label(root,text="two",bg="blue",fg="white")
# two.pack(fill=X)

# three=Label(root,text="three",bg="green",fg="white")
# three.pack(side=LEFT,fill=Y)


# root.mainloop()