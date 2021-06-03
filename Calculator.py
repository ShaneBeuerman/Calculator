#Calculator
import tkinter

def badInput():
    print("Bad")

def buttonPress():
    print("Press Button")
    global display
    display.config(text="n")

def equalsButtonPress():
    print("Press Equals Button")

GUI = tkinter.Tk()
display = tkinter.Label(text="")
display.grid(row=0,column=4)
b1 = tkinter.Button(text="  1  ", command=buttonPress)
b1.grid(row=1, column=0)
b2 = tkinter.Button(text="  2  ", command=buttonPress)
b2.grid(row=1, column=1)
b3 = tkinter.Button(text="  3  ", command=buttonPress)
b3.grid(row=1, column=2)
b4 = tkinter.Button(text="  4  ", command=buttonPress)
b4.grid(row=2, column=0)
b5 = tkinter.Button(text="  5  ", command=buttonPress)
b5.grid(row=2, column=1)
b6 = tkinter.Button(text="  6  ", command=buttonPress)
b6.grid(row=2, column = 2)
b7 = tkinter.Button(text="  7  ", command=buttonPress)
b7.grid(row=3, column=0)
b8 = tkinter.Button(text="  8  ", command=buttonPress)
b8.grid(row=3, column=1)
b9 = tkinter.Button(text="  9  ", command=buttonPress)
b9.grid(row=3, column=2)
bPlus = tkinter.Button(text="  +  ", command=buttonPress)
bPlus.grid(row=1, column=3)
bMinus = tkinter.Button(text="  -  ", command=buttonPress)
bMinus.grid(row=2,column=3)
bEquals = tkinter.Button(text="  =  ", command=equalsButtonPress)
bEquals.grid(row=3, column=3)
GUI.mainloop()



