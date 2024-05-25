import random, string
from tkinter import *
 
 
root =Tk()
root.geometry("400x400") 
 
root.title("Random Password Generator")
 
 
output_pass = StringVar()
 
all_combi = [string.ascii_uppercase, string.digits, string.ascii_lowercase, string.punctuation]  
 
def randPassGen():
    password = "" 
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi) 
        password = password + random.choice(char_type)
     
    output_pass.set(password)

 
pass_head = Label(
    root, 
    text = 'Password Length', 
    font = ("arial", "14", "bold")).pack(pady=25)
 
pass_len = IntVar() 
length = Spinbox(
    root, 
    from_ = 4, 
    to_ = 32 , 
    textvariable = pass_len , 
    width = 24, 
    font='arial 16').pack()
 

 
Button(
    root, 
    command = randPassGen, 
    text = "Generate Password", 
    font=("arial", "10", "bold"), 
    bg='lightblue', fg='black', 
    activebackground="teal", 
    padx=5, 
    pady=5 ).pack(pady= 20)
 
pass_label = Label(
    root, 
    text = 'Random Generated Password', 
    font = ("arial", "14", "bold")).pack(pady="30 10")
Entry(
    root , 
    textvariable = output_pass, 
    width = 24, 
    font='arial 16').pack(pady=25)
 

 
root.mainloop()  
