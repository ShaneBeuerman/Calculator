#Calculator
import tkinter

def buttonPress(symbol):
    global display
    global displayText
    displayText += symbol
    display.config(text=displayText)

def equalsButtonPress():
    global display
    global displayText
    try:
        displayText = str(eval(displayText))
    except:
        displayText = ""
    display.config(text= displayText)

def clearButtonPress():
    global display
    global displayText
    displayText = ""
    display.config(text= displayText)

displayText = ""
GUI = tkinter.Tk()
GUI.wm_title("Calculator")
display = tkinter.Label(text=displayText)
display.grid(row=0,column=4)
b1 = tkinter.Button(text="  1  ", command= lambda cur = "1": buttonPress(cur))
b1.grid(row=3, column=0)
b2 = tkinter.Button(text="  2  ", command= lambda cur = "2": buttonPress(cur))
b2.grid(row=3, column=1)
b3 = tkinter.Button(text="  3  ", command= lambda cur = "3": buttonPress(cur))
b3.grid(row=3, column=2)
b4 = tkinter.Button(text="  4  ", command= lambda cur = "4": buttonPress(cur))
b4.grid(row=2, column=0)
b5 = tkinter.Button(text="  5  ", command= lambda cur = "5": buttonPress(cur))
b5.grid(row=2, column=1)
b6 = tkinter.Button(text="  6  ", command= lambda cur = "6": buttonPress(cur))
b6.grid(row=2, column = 2)
b7 = tkinter.Button(text="  7  ", command= lambda cur = "7": buttonPress(cur))
b7.grid(row=1, column=0)
b8 = tkinter.Button(text="  8  ", command= lambda cur = "8": buttonPress(cur))
b8.grid(row=1, column=1)
b9 = tkinter.Button(text="  9  ", command= lambda cur = "9": buttonPress(cur))
b9.grid(row=1, column=2)
bPlus = tkinter.Button(text="  +  ", command= lambda cur = "+": buttonPress(cur))
bPlus.grid(row=1, column=3)
bMinus = tkinter.Button(text="  -  ", command=lambda cur = "-": buttonPress(cur))
bMinus.grid(row=2,column=3)
bEquals = tkinter.Button(text="  =  ", command=equalsButtonPress)
bEquals.grid(row=3, column=3)
bDivide = tkinter.Button(text="  /  ", command=lambda cur = "/": buttonPress(cur))
bDivide.grid(row=1, column=4)
bMultiply = tkinter.Button(text="  *  ", command=lambda cur = "*": buttonPress(cur))
bMultiply.grid(row=2, column=4)
bClear = tkinter.Button(text="Clear", command = clearButtonPress)
bClear.grid(row=3, column=4)
GUI.mainloop()