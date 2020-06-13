from tkinter import*

root=Tk()
root.geometry("354x500")
root.title("CALCULATOR")
label = Label(root,text="CALCULATOR BY PC",bg='white',font=("Courier New",32,'italic'))
label.pack(side=TOP)
root.config(background='black')

textin=StringVar()
operator=""

def clickbut(number):   
     global operator
     operator=operator+str(number)
     textin.set(operator)

def equlbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''
def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''     
def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''
def equlbut():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''    

def clrbut():
     textin.set('')

     
text=Entry(root,font=("Courier New",12,'bold'),textvar=textin,width=25,bd=5,bg='white')
text.pack()

but1=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=90,y=100)

but2=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=170,y=100)

but3=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=260,y=100)

but4=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=350,y=100)

but5=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=10,y=180)

but6=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=90,y=180)

but7=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=170,y=180)

but8=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=260,y=180)

but9=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=10,y=250)

but0=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=100)

butdot=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=90,y=340)

butpl=Button(root,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butpl.place(x=10,y=340)

butsub=Button(root,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butsub.place(x=350,y=340)

butml=Button(root,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
butml.place(x=170,y=340)

butdiv=Button(root,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=260,y=340)

butclear=Button(root,padx=10,pady=50,bd=4,bg='white',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=350,y=180)

butequal=Button(root,padx=100,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=90,y=250)
root.mainloop()