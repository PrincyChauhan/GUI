from tkinter import*
import tkinter.messagebox

root=Tk()

tkinter.messagebox.showinfo("Window Title","I am Princy Chauhan")

answer=tkinter.messagebox.askquestion("question1","Do you know Princy Chauhan?")

if answer=='yes':
    print("wow! It's great!!!")

root.mainloop()