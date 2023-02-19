import tkinter
from tkinter import OptionMenu
from tkinter import StringVar
from tkinter import END
from random import randint
from math import sqrt

calculation = ""


def newWin():
    global calc
    window.destroy()

    
    calc = tkinter.Tk()
    calc.iconbitmap(r'favicon.ico')
    calc.geometry("525x382")
    calc.title("Calculator")


    def add_to_calc(symbol):
        global calculation
        calculation += str(symbol)
        text_result.delete(1.0,"end")
        text_result.insert(1.0, calculation)
        

    def eval_to_calc():
        global calculation
        try:
            calculation = str(eval(calculation))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
            
        except:
            clear_field()
            text_result.insert(1.0, "Error")
            
    def clear_field():
        global calculation
        calculation = ""
        text_result.delete(1.0,"end")
        text_result.configure(state=tkinter.NORMAL)

    text_result = tkinter.Text(calc, height=2, width=29, font=("Arial", 24),bg="gray",fg="white")
    text_result.grid(columnspan=5)
    

    btn1 = tkinter.Button(calc, text="1", command=lambda: add_to_calc(1), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn1.grid(row = 2, column=1)
    btn2 = tkinter.Button(calc, text="2", command=lambda: add_to_calc(2), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn2.grid(row = 2, column=2)
    btn3 = tkinter.Button(calc, text="3", command=lambda: add_to_calc(3), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn3.grid(row = 2, column=3)
    btn4 = tkinter.Button(calc, text="4", command=lambda: add_to_calc(4), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn4.grid(row = 3, column=1)
    btn5 = tkinter.Button(calc, text="5", command=lambda: add_to_calc(5), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn5.grid(row = 3, column=2)
    btn6 = tkinter.Button(calc, text="6", command=lambda: add_to_calc(6), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn6.grid(row = 3, column=3)
    btn7 = tkinter.Button(calc, text="7", command=lambda: add_to_calc(7), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn7.grid(row = 4, column=1)
    btn8 = tkinter.Button(calc, text="8", command=lambda: add_to_calc(8), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn8.grid(row = 4, column=2)
    btn9 = tkinter.Button(calc, text="9", command=lambda: add_to_calc(9), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn9.grid(row = 4, column=3)
    btn0 = tkinter.Button(calc, text="0", command=lambda: add_to_calc(0), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn0.grid(row = 5, column=2)

    btn_plus = tkinter.Button(calc, text="+", command=lambda: add_to_calc("+"), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn_plus.grid(row = 2, column=4)
    btn_minus = tkinter.Button(calc, text="-", command=lambda: add_to_calc("-"), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn_minus.grid(row = 3, column=4)
    btn_mult = tkinter.Button(calc, text="*", command=lambda: add_to_calc("*"), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn_mult.grid(row = 4, column=4)
    btn_div = tkinter.Button(calc, text="/", command=lambda: add_to_calc("/"), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn_div.grid(row = 5, column=4)

    btn_parenth1 = tkinter.Button(calc, text="(", command=lambda: add_to_calc("("), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn_parenth1.grid(row = 5, column=1)
    btn_parenth2 = tkinter.Button(calc, text=")", command=lambda: add_to_calc(")"), width=11, height=2, font=("Arial", 14),bg="black",fg="white")
    btn_parenth2.grid(row = 5, column=3)

    btn_eq = tkinter.Button(calc, text="=", command=eval_to_calc, width=23, height=2, font=("Arial", 14),bg="black",fg="white")
    btn_eq.grid(row = 6, column=1, columnspan=2)
    btn_clr = tkinter.Button(calc, text="C", command=clear_field, width=23, height=2, font=("Arial", 14),bg="black",fg="white")
    btn_clr.grid(row = 6, column=3, columnspan=2)

    calc.resizable(False,False)
    calc.mainloop()


    window.destroy()
    unitWin = tkinter.Tk()
    unitWin.iconbitmap(r'favicon.ico')
    unitWin.geometry("400x500")
    unitWin.title("Unit Conversion")

    clicked = StringVar()
    clicked.set("Choose a Unit")
    clicked2 = StringVar()
    clicked2.set("Choose a Unit")

    def convert():
        if clicked.get() == "mg to g":
            val = eval(tb1.get(1.0, "end"))
            val /= 1000
            tb1.delete(1.0, "end")
            tb1.insert(1.0, val,"g")
        elif clicked.get() == "g to kg":
            val = eval(tb1.get(1.0, "end"))
            val /= 1000
            tb1.delete(1.0, "end")
            tb1.insert(1.0, val,"kg")
    def convert2():
        if clicked2.get() == "mm to cm":
            val1 = eval(tb2.get(1.0, "end"))
            val1 /= 1000
            tb2.delete(1.0, "end")
            tb2.insert(1.0, val1,"kg")
        elif clicked.get() == "g to kg":
            val1 = eval(tb2.get(1.0, "end"))
            val1 /= 10
            tb2.delete(1.0, "end")
            tb2.insert(1.0, val1)
        elif clicked2.get() == "cm to m":
            val1 = eval(tb2.get(1.0, "end"))
            val1 /= 100
            tb2.delete(1.0, "end")
            tb2.insert(1.0, val1)
        elif clicked2.get() == "m to km":
            val1 = eval(tb2.get(1.0, "end"))
            val1 /= 100
            tb2.delete(1.0, "end")
            tb2.insert(1.0, val1)

    title = tkinter.Label(unitWin, text="Unit Converter", width=300, font=("Arial",15))
    title.pack()

    mass = tkinter.Label(unitWin, text="Mass Conversion:", font=("Arial", 12))
    mass.place(x=20, y=60)
    tb1 = tkinter.Text(unitWin,height=1,width=18,font=("Arial",10))
    tb1.place(x=22, y=95)
    drop1 = OptionMenu(unitWin, clicked, "mg to g","g to kg")
    drop1.place(x=153,y=57)
    btn = tkinter.Button(unitWin,text="Convert", width=15, command=convert)
    btn.place(x=155 ,y=92)

    len = tkinter.Label(unitWin, text="Length Conversion:", font=("Arial", 12))
    len.place(x=20, y=120)
    tb2 = tkinter.Text(unitWin,height=1,width=18,font=("Arial",10))
    tb2.place(x=22, y=155)
    drop2 = OptionMenu(unitWin, clicked2, "mm to cm","cm to m","m to km")
    drop2.place(x=153,y=117)
    btn2 = tkinter.Button(unitWin,text="Convert", width=15, command=convert2)
    btn2.place(x=155 ,y=152)

    

    unitWin.mainloop()
def ranWin():
    window.destroy()

    random = tkinter.Tk()
    random.iconbitmap(r'favicon.ico')
    random.config(bg="gray")
    random.geometry("400x300")
    random.title("Random Number Generator")

    def Generate():
        global ran_num
        upper = int(text1.get("1.0", END))
        lower = int(text2.get("1.0", END))
        ran_num = str(randint(upper,lower))
        result.configure(text=ran_num)
      


    label = tkinter.Label(random, text = "Number Generator", width=300, font=("Arial", 17),bg="black",fg="white")
    label.pack()

    field1 = tkinter.Label(random, text="Enter upper limit:",font=("Arial", 13),bg="black",fg="white")
    field1.place(x=85, y=80)
    text1 = tkinter.Text(random, height=1,width=10,font=("Arial", 13))
    text1.place(x=215, y=80)
    field2 = tkinter.Label(random, text="Enter lower limit:",font=("Arial", 13),bg="black",fg="white")
    field2.place(x=85, y=120)
    text2 = tkinter.Text(random, height=1,width=10,font=("Arial", 13))
    text2.place(x=215, y=120)



    but1 = tkinter.Button(random,text="Generate", font=("Arial", 13),command=Generate,bg="black",fg="white")
    but1.place(x=150,y=160)

    result = tkinter.Label(random,font=("Arial",15),justify="center",bg="gray",fg="white")
    result.place(x=190,y=215,anchor="center")

    random.resizable(False,False)
    random.mainloop()
def graWin():
    window.destroy()

    graph = tkinter.Tk()
    graph.iconbitmap(r'favicon.ico')
    graph.config(bg="gray")
    graph.geometry("500x250")
    graph.title("Graph Plotter")
    graph.resizable(False,False)
    
    label = tkinter.Label(graph, text = "Quadratic Equation Solver", width=300, font=("Arial", 17),bg="black",fg="white")
    label.pack()

    def quad():
        a = int(a_val.get("1.0",END))
        b = int(b_val.get("1.0",END))
        c = int(c_val.get("1.0",END))
        try:
            dis = (b**2) - (4 * a * c)
            ans1 = (-b-sqrt(dis))/(2*a)
            ans2 = (-b+sqrt(dis))/(2*a)
        except:
            res1.configure(text="Invalid Equation")
        else:
            res1.configure(text=ans1)
            res2.configure(text=ans2)

    a_val = tkinter.Text(graph,font=("Arial",13), height=1,width=4)
    a_val.place(x=120,y=50)
    xsqlab = tkinter.Label(graph,text="X² +",bg="gray",font=("Arial",14))
    xsqlab.place(x=170,y=50)
    b_val = tkinter.Text(graph,font=("Arial",13), height=1,width=4)
    b_val.place(x=220,y=50)
    xlab = tkinter.Label(graph,text="X +",bg="gray",font=("Arial",14))
    xlab.place(x=270,y=50)
    c_val = tkinter.Text(graph,font=("Arial",13), height=1,width=4)
    c_val.place(x=320,y=50)

  
    but = tkinter.Button(graph,text="Solve",font=("Arial",12),command=quad,bg="black",fg="White")
    but.place(x=215,y=90)

    lab1 = tkinter.Label(graph,font=("Arial",13),text="The roots are:",bg="black",fg="white")
    lab1.place(x=187,y=130)
    res1 = tkinter.Label(graph,font=("Arial",15),bg="gray")
    res1.place(x=235,y=170,anchor="center")
    res2 = tkinter.Label(graph,font=("Arial",15),bg="gray")
    res2.place(x=235,y=200,anchor="center")
   


    graph.mainloop()


window = tkinter.Tk()
window.geometry("400x500")
window.configure(bg="gray")
window.title("Home")
window.iconbitmap(r'favicon.ico')

label = tkinter.Label(window, text = "Math All-In-One", width=300, font=("Arial", 15),bg="black",fg="white")
text = tkinter.Label(window, text = "Please select an option to continue: ", width=300,font=("Arial", 13),bg="black",fg="white")
label.pack(anchor="center")
text.pack()

b1 = tkinter.Button(window, text="Basic Operations",font=("Arial", 11),command=newWin,bg="black",fg="white")
b1.place(x=135,y=90)

b2 = tkinter.Button(window, text="Number Generator",width=13,font=("Arial", 11),command=ranWin,bg="black",fg="white")
b2.place(x=135,y=160)

b3 = tkinter.Button(window, text="Equation Solver",width=13,font=("Arial", 11),bg="black",fg="white",command=graWin)
b3.place(x=135,y=230)

b4 = tkinter.Button(window, text="Exit",width=13,font=("Arial", 11), command=window.destroy,bg="black",fg="white")
b4.place(x=135,y=300)


credit = tkinter.Label(window, text = "Built by: Niteesh Kumar",font=("Arial", 10),bg="black",fg="white")
credit.place(x=130,y=460)

window.resizable(False,False)
window.mainloop()



