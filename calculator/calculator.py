#Test 
#Please do not use as it is not correct
#Пожалуйста, не используйте, так как это неверно
import tkinter as tk
from tkinter import StringVar 

bg = {"bg" :"#424242" , "fg" : "#F1F8E9"}

base = ""

def callback(event):
    print ("clicked at"), event.x, event.y

def press(num):
    global base
    base = base + str(num)
    asli.set(base)


def equalpress(): 
    try: 
        global base
        total = str(eval(base)) 
        asli.set(total) 
        base = "" 
    except: 
        asli.set(" error ") 
        base = "" 
  
###### ROOT MAIN ######

root = tk.Tk()
root.title("")
root.minsize(180 , 120)


###### Entery ######
asli = StringVar()
tk.Entry(root , textvariable=asli).grid(row= 0 ,column=0 ,rowspan= 1, columnspan=6 , sticky=tk.W+tk.E+tk.S)

###### Button COLUMN-1 ######

tk.Button(root , text= 1 , cnf=bg ,command=lambda: press(1), width=5 ).grid(row=1 , column =0)
tk.Button(root , text= 2 , cnf=bg ,command=lambda: press(2), width=5 ).grid(row=1 , column =1)
tk.Button(root , text= 3 , cnf=bg ,command=lambda: press(3), width=5 ).grid(row=1, column =2)

tk.Button(root , text= "÷" , cnf=bg ,command=lambda: press("÷"), width=5 ).grid(row=1 , column =3)

###### Button COLUMN-2 ######

tk.Button(root , text= 4 , cnf=bg ,command=lambda: press(4), width=5 ).grid(row=2 , column =0)
tk.Button(root , text= 5 , cnf=bg ,command=lambda: press(5), width=5 ).grid(row=2 , column =1)
tk.Button(root , text= 6 , cnf=bg ,command=lambda: press(6), width=5 ).grid(row=2 , column =2)
tk.Button(root , text= "×" , cnf=bg ,command=lambda: press("×"), width=5 ).grid(row=2 , column =3)

###### Button COLUMN-3 ######

tk.Button(root , text= 7 , cnf=bg ,command=lambda: press(7), width=5 ).grid(row=3 , column =0)
tk.Button(root , text= 8 , cnf=bg ,command=lambda: press(8), width=5 ).grid(row=3 , column =1)
tk.Button(root , text= 9 , cnf=bg ,command=lambda: press(9), width=5 ).grid(row=3 , column =2)
tk.Button(root , text= "-" , cnf=bg ,command=lambda: press("-"), width=5 ).grid(row=3 , column =3)


###### Button COLUMN-4 ######

tk.Button(root , text= "+" , cnf=bg ,command=lambda: press("+"), width=5 ).grid(row=4 , column =3)
tk.Button(root , text= 0 , cnf=bg ,command=lambda: press(0), width=5 ).grid(row=4 , column =0 , columnspan=2 , sticky=tk.W+tk.E)
tk.Button(root , text= "=" , cnf=bg ,command=equalpress, width=5 ).grid(row=4 , column =2)

root.mainloop()