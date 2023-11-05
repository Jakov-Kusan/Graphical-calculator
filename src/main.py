print("Importing modules")
try:
    from tkinter import*
    import tkinter.font as tkFont

except:
    print("Unable to import modules")
    exit()

window = Tk()   
window.geometry("269x380")  
window.title("Calculator")
window.resizable(False,False)

# Variables
calculation = ''
answer = ''

# Functions
def calculationAdd(numberOrOperator):
    global calculatorGui
    global calculation

    if len(calculation)<13:
        calculation= calculation + numberOrOperator
        calculatorGui.config(text=calculation)  

def calculate():
    global calculation
    global answer
    global calculatorGui2
    try:
        answer = eval(calculation)
        calculatorGui2.config(text=answer)
    except:
        calculatorGui2.config(text="Invalid syntax")
    calculation = ''



# LABELS

calculatorGui = Label(window, text = '',font=("", 25) )
calculatorGui.place(x = 10,y = 10)

calculatorGui2 = Label(window, text = '',font=("", 25) )
calculatorGui2.place(x = 10,y = 50)

# BUTTONS

buttonDivide = Button(window, text = "/",command=lambda: calculationAdd("/"),height=3,width=5)
buttonDivide.place(x = 67+67+67,y = 100)

buttonMultiply = Button(window, text = "*",command=lambda: calculationAdd("*"),height=3,width=5)
buttonMultiply.place(x = 67+67+67,y = 170)

buttonSubtract = Button(window, text = "-",command=lambda: calculationAdd("-"),height=3,width=5)
buttonSubtract.place(x = 67+67+67,y = 170+70)

buttonAdd= Button(window, text = "+",command=lambda: calculationAdd("+"),height=3,width=5)
buttonAdd.place(x = 67+67+67,y = 170+70+70)

buttonCalculate= Button(window, text = "=",command=calculate,height=3,width=5)
buttonCalculate.place(x = 67+67,y = 170+70+70)

buttonDecimal= Button(window, text = ".",command=lambda: calculationAdd("."),height=3,width=5)
buttonDecimal.place(x = 67,y = 170+70+70)

button9 = Button(window, text = "9",command=lambda: calculationAdd("9"),height=3,width=5)
button9.place(x = 67+67,y = 100)

button8 = Button(window, text = "8",command=lambda: calculationAdd("8"),height=3,width=5)
button8.place(x = 67,y = 100)

button7 = Button(window, text = "7",command=lambda: calculationAdd("7"),height=3,width=5)
button7.place(x = 0,y = 100)

button6 = Button(window, text = "6",command=lambda: calculationAdd("6"),height=3,width=5)
button6.place(x = 67+67,y = 170)


button5 = Button(window, text = "5",command=lambda: calculationAdd("5"),height=3,width=5)
button5.place(x = 67,y = 170)

button4 = Button(window, text = "4",command=lambda: calculationAdd("4"),height=3,width=5)
button4.place(x = 0,y = 170)

button3 = Button(window, text = "3",command=lambda: calculationAdd("3"),height=3,width=5)
button3.place(x = 67+67,y = 170+70)

button2 = Button(window, text = "2",command=lambda: calculationAdd("2"),height=3,width=5)
button2.place(x = 67,y = 170+70)

button1 = Button(window, text = "1",command=lambda: calculationAdd("1"),height=3,width=5)
button1.place(x = 0,y = 170+70)

button0 = Button(window, text = "0",command=lambda: calculationAdd("0"),height=3,width=5)
button0.place(x = 0,y = 170+70+70)


window.mainloop()  