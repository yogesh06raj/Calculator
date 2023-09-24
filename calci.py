from tkinter import *
import tkinter.messagebox
import math



def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay() :
    global operator
    operator=""
    text_Input.set("")

def btnEqual():
    try:
        global operator
        sumup=str(eval(operator))
        text_Input.set(sumup)
        operator=sumup
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")


def btnDelete():
    global operator
    operator=operator[:-1]
    text_Input.set(operator)

def btnSquareRoot():
   try:
        operator = math.sqrt(float(text_Input.get()))
        text_Input.set(str(operator))

   except:
        tkinter.messagebox.showinfo("Error", "Input Error")
       

calc = Tk()
calc.title("Calculator")
operator=""
text_Input =StringVar()

txtDisplay = Entry(calc,font=('arial black', 20,'bold') , textvariable=text_Input, bd=30, insertwidth=6,
bg="skyblue", justify='right').grid(columnspan=6)

Clear=Button(calc,font=('arial black', 20,'bold'),
            text="CE",height="1",width="4",command= btnClearDisplay, bg="grey").grid(row=1,column=0)

SquareRoot=Button(calc,font=('arial black', 20,'bold'),
            text="√x",height="1",width="4",command= btnSquareRoot, bg="cyan").grid(row=1,column=2)

Delete=Button(calc,font=('arial black', 20,'bold'),
            text="DEL",height="1",width="4",command= btnDelete, bg="red").grid(row=1,column=1)

#===================================================================================

btn1=Button(calc,font=('arial black', 20,'bold'),
            text="1",height="1",width="4",command=lambda:btnClick(1), bg="powder blue",).grid(row=2,column=0)

btn2=Button(calc,font=('arial black', 20,'bold'),
            text="2",height="1",width="4",command=lambda:btnClick(2), bg="powder blue").grid(row=2,column=1)

btn3=Button(calc,font=('arial black', 20,'bold'),
            text="3",height="1",width="4",command=lambda:btnClick(3), bg="powder blue").grid(row=2,column=2)

Addition=Button(calc,font=('arial black', 20,'bold'),
            text="+",height="1",width="4",command=lambda:btnClick("+"), bg="cyan").grid(row=1,column=3)

#===================================================================================

btn4=Button(calc,font=('arial black', 20,'bold'),
            text="4",height="1",width="4",command=lambda:btnClick(4), bg="powder blue").grid(row=3,column=0)

btn5=Button(calc,font=('arial black', 20,'bold'),
            text="5",height="1",width="4",command=lambda:btnClick(5), bg="powder blue").grid(row=3,column=1)

btn6=Button(calc,font=('arial black', 20,'bold'),
            text="6",height="1",width="4",command=lambda:btnClick(6), bg="powder blue").grid(row=3,column=2)

Subtraction=Button(calc,font=('arial black', 20,'bold'),
            text="-",height="1",width="4",command=lambda:btnClick("-"), bg="cyan").grid(row=2,column=3)

#===================================================================================

btn7=Button(calc,font=('arial black', 20,'bold'),
            text="7",height="1",width="4",command=lambda:btnClick(7), bg="powder blue").grid(row=4,column=0)

btn8=Button(calc,font=('arial black', 20,'bold'),
            text="8",height="1",width="4",command=lambda:btnClick(8), bg="powder blue").grid(row=4,column=1)

btn9=Button(calc,font=('arial black', 20,'bold'),
            text="9",height="1",width="4",command=lambda:btnClick(9), bg="powder blue").grid(row=4,column=2)

Multiplication=Button(calc,font=('arial black', 20,'bold'),
            text="*",height="1",width="4",command=lambda:btnClick("*"), bg="cyan").grid(row=3,column=3)

#===================================================================================


btn0=Button(calc,font=('arial black', 20,'bold'),
            text="0",height="1",width="4",command=lambda:btnClick(0), bg="powder blue").grid(row=5,column=1)

EQUALS=Button(calc,padx=12,font=('arial black', 18,'bold'),
            text="=",command=btnEqual, bg="green").grid(row=5,column=2,columnspan=2, sticky="ew")

Division=Button(calc,font=('arial black', 20,'bold'),
            text="/",height="1",width="4",command=lambda:btnClick("/"), bg="cyan").grid(row=4,column=3)

Decimal=Button(calc,font=('arial black', 20,'bold'),
            text=".",height="1",width="4",command=lambda:btnClick("."), bg="powder blue").grid(row=5,column=0)

#===================================================================================

calc.mainloop()
