from tkinter import*
root=Tk()#Instantiation of Tk()class

def button_response(event): #creating function for button
    b = event.widget
    text = b['text']
    if text == "=":
        try:
            the_value = entry.get()
            answer=eval(the_value)
            entry.delete(0,END)
            entry.insert(0,answer)
        except SyntaxError:
            Serror = "Syntax Error"
            entry.delete(0,END)
            entry.insert(0,Serror)
        except ZeroDivisionError:
            Zerror = "Undifned"
            entry.delete(0,END)
            entry.insert(0,Zerror)
        return
    else:
        entry.insert(END,text)


def button_clear():
    entry.delete(0,END)



root.resizable(0,0) #shows that the window is resizable or not
value=StringVar()
root['bg'] = ["#42f593"]
entry=Entry(root,width=15,bg="black",fg="light green",font=("verdana",20,"bold"),justify="right",textvariable=value,bd=25)
entry.pack(side=TOP,pady=8,padx=20)
#entry.grid(column=1,row=0,pady=10)

frame1 = LabelFrame(root,bg='#97b4f7')
frame1.pack()


temp = 1

for i in range(0,3):
    for j in range(0,3):
        btn = Button(frame1,text=str(temp),font=('arial',25,'bold'),bg='white',activebackground="grey",bd=10,padx=20,pady=9)
        btn.grid(column=j,row=i)
        temp=temp+1
        btn.bind('<Button-1>',button_response)


C = Button(frame1,text="C",font=('arial',25,'bold'),activebackground="grey",bg='white',bd=10,padx=20,pady=9,command=button_clear)
C.grid(column=4,row=0)

sign1= Button(frame1,text="+",font=('arial',25,'bold'),activebackground="grey",bg='white',bd=10,padx=24,pady=9)
sign1.grid(column=4,row=1)


sign2 = Button(frame1,text="-",font=('arial',25,'bold'),activebackground="grey",bg='white',bd=10,padx=27,pady=9)
sign2.grid(column=4,row=2)


sign3 = Button(frame1,text="*",font=('arial',25,'bold'),activebackground="grey",bg='white',bd=10,padx=25,pady=9)
sign3.grid(column=4,row=3)


sign4 = Button(frame1,text="/",font=('arial',25,'bold'),activebackground="grey",bg='white',bd=10,padx=25,pady=9)
sign4.grid(column=2,row=3)



sign5 = Button(frame1,text="=",font=('arial',25,'bold'),activebackground="grey",bg='white',bd=10,padx=20,pady=9)
sign5.grid(column=1,row=3)

sign6 = Button(frame1,text="0",font=('arial',25,'bold'),activebackground="grey",bg='white',bd=10,padx=20,pady=9)
sign6.grid(column=0,row=3)

sign1.bind('<Button-1>',button_response)
sign2.bind('<Button-1>',button_response)
sign3.bind('<Button-1>',button_response)
sign4.bind('<Button-1>',button_response)
sign5.bind('<Button-1>',button_response)
sign6.bind('<Button-1>',button_response)



root.mainloop()
