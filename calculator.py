from tkinter import * 

win = Tk() 
win.title("GUI Calculator") 
win.resizable(False, False) 


def button_press(num):
    global exp
    exp= input_text.get()
    exp= str(exp) + str(num)
    input_text.set(exp)

def button_oper(opr):
    global exp
    exp = input_text.get()
    exp= str(exp) + str(opr)
    input_text.set(exp)
    global oper
    oper = opr

def clr_scr():
    global exp
    input_text.set("")
    exp = ""

def equal(event):
    global display
    global oper
    global exp
    exp = input_text.get()
    input_text.set("")
    result = float(eval(exp))
    exp = result
    display.insert(0, result)
    input_text.set(result)


display_frame = LabelFrame(win,relief=SUNKEN, padx=2, pady=2)
display_frame.grid(row=0, column=0, columnspan=4, padx=2, pady=4)

input_text = StringVar()

display = Entry(display_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=22, bg="#eee", bd=0, justify=RIGHT)
display.pack(ipady= 12) 


button_1 = Button(win, font=(15), padx=30, pady=30, text="1", bg="Lightgrey", command=lambda: button_press(1))
button_2 = Button(win, font=(15), padx=30, pady=30, text="2", bg="Lightgrey", command=lambda: button_press(2))
button_3 = Button(win, font=(15), padx=30, pady=30, text="3", bg="Lightgrey", command=lambda: button_press(3))
button_4 = Button(win, font=(15), padx=30, pady=30, text="4", bg="Lightgrey", command=lambda: button_press(4))
button_5 = Button(win, font=(15), padx=30, pady=30, text="5", bg="Lightgrey", command=lambda: button_press(5))
button_6 = Button(win, font=(15), padx=30, pady=30, text="6", bg="Lightgrey", command=lambda: button_press(6))
button_7 = Button(win, font=(15), padx=30, pady=30, text="7", bg="Lightgrey", command=lambda: button_press(7))
button_8 = Button(win, font=(15), padx=30, pady=30, text="8", bg="Lightgrey", command=lambda: button_press(8))
button_9 = Button(win, font=(15), padx=30, pady=30, text="9", bg="Lightgrey", command=lambda: button_press(9))
button_0 = Button(win, font=(15), padx=30, pady=30, text="0", bg="Lightgrey", command=lambda: button_press(0))
button_add = Button(win, font=(15), padx=30, pady=30, text="+", bg="Lightgrey", command=lambda: button_oper("+"))
button_sub = Button(win, font=(15), padx=30, pady=30, text="- ", bg="Lightgrey", command=lambda: button_oper("-"))
button_div = Button(win, font=(15), padx=30, pady=30, text="/ ", bg="Lightgrey", command=lambda: button_oper("/"))
button_mul = Button(win, font=(15), padx=30, pady=30, text="* ", bg="Lightgrey", command=lambda: button_oper("*"))
button_equal = Button(win, font=(15), padx=30, pady=30, text="=", bg="Lightgrey", command=lambda: equal(""))
button_clear = Button(win, font=(15), padx=30, pady=30, text="C", bg="Lightgrey", command=clr_scr)
button_dec = Button(win, font=(15), padx=30, pady=30, text=" .", bg="Lightgrey", command=lambda: button_press("."))


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_div.grid(row=3, column=3)

button_equal.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_dec.grid(row=4, column=2)
button_mul.grid(row=4, column=3)

win.bind("<Return>", equal)

win.mainloop()