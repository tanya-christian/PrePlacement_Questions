from tkinter import *

#main window
root = Tk()
root.title("Calculator")
root.geometry('600x400')

#MenuBar
def close():
    root.destroy()
    
menu = Menu(root)
item = Menu(menu)
item.add_command(label="Exit",command=close)
menu.add_cascade(label="File", menu=item)
root.config(menu=menu)

#Label
lbl1 = Label(root,text="Enter Number",font=("Arial", 12, "bold"))
lbl1.grid(row=0,column=1)
#textbox
num1 = Entry(root,width=20)
num1.grid(row=0,column=2,padx=5, pady=5)
#label
lbl2 = Label(root, text="Enter Number",font=("Arial", 12, "bold"))
lbl2.grid(row=1,column=1)
#textbox
num2 = Entry(root,width=20)
num2.grid(row=1,column=2,padx=5, pady=5)

#button
def add():
    n1 = int(num1.get())
    n2 = int(num2.get())
    ans = n1+n2
    txt.configure(text="Answer is " + str(ans))

btn1 = Button(root,text="+",command=add,font=("Arial", 10, "bold"))
btn1.grid(row=2,column=1,ipadx=10, ipady=5, padx=5, pady=5)

def sub():
    n1 = int(num1.get())
    n2 = int(num2.get())
    ans = n1-n2
    txt.configure(text="Answer is " + str(ans))
btn2 = Button(root,text="-",command=sub,font=("Arial", 10, "bold"))
btn2.grid(row=2,column=2,ipadx=10, ipady=5, padx=5, pady=5)

def mul():
    n1 = int(num1.get())
    n2 = int(num2.get())
    ans = n1*n2
    txt.configure(text="Answer is " + str(ans))
btn3 = Button(root,text="*",command=mul,font=("Arial", 10, "bold"))
btn3.grid(row=2,column=3,ipadx=10, ipady=5, padx=5, pady=5)

def div():
    n1 = int(num1.get())
    n2 = int(num2.get())
    ans = n1//n2
    txt.configure(text="Answer is " + str(ans))
btn4 = Button(root,text="/",command=div,font=("Arial", 10, "bold"))
btn4.grid(row=2,column=4,ipadx=10, ipady=5, padx=5, pady=5)

#label
txt = Label(root,font=("Arial", 12, "bold"))
txt.grid(row=3, column=2)
root.mainloop()
