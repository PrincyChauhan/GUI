#========MENU BAR============
from tkinter import*
def doNothing():
    print("ok,ok I won't!")

root = Tk()

menu=Menu(root)
root.config(menu=menu)

SubMenu=Menu(menu)
menu.add_cascade(label="File",menu=SubMenu) 

SubMenu.add_command(label="New Project",command=doNothing)
SubMenu.add_separator()

SubMenu.add_command(label="Exit",command=doNothing)

editMenu=Menu(menu)
menu.add_cascade(label="Redo",command=doNothing)

#=================TOOL BAR======================

toolbar=Frame(root,bg="pink")

insertbutt=Button(toolbar,text="Inserting..",command=doNothing)
insertbutt.pack(side=LEFT,padx=2,pady=2)

printbutt=Button(toolbar,text="Print",command=doNothing)
printbutt.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)


#============STATUS BAR================

status=Label(root,text="Preparing for University exam..")
status.pack(side=BOTTOM,fill=X)
root.mainloop()
