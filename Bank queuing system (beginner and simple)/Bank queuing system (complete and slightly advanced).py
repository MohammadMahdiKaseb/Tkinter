import tkinter as tk
from datetime import datetime


def turn():
    global n
    n += 1

    d = datetime.now()
    l1.config(text=d.strftime("%B-%d-%Y"), )
    s1.config(text=d.strftime("%I-%M-%S %p"))
    r1.config(text=d.strftime("%A"))
    numbers.append(n + 1)
    print(numbers)
    a1.config(text=numbers[-1])


def tpo1():
    if numbers:
        to1.config(text=numbers.pop(0))


def tpo2():
    if numbers:
        to2.config(text=numbers.pop(0))


def tpo3():
    if numbers:
        to3.config(text=numbers.pop(0))


root = tk.Tk()
n = -1
numbers = []

l1 = tk.Label(root, text="", fg="red", bg="black")
l1.grid()

s1 = tk.Label(root, text="")
s1.grid(row=0, column=0)

r1 = tk.Label(root, text="")
r1.grid(row=1, column=0)

a1 = tk.Label(root, text="")
a1.grid(row=2, column=0)

b1 = tk.Button(root, text="get turn", command=turn)
b1.grid(row=3, column=0)

tp = tk.Toplevel(root)

tp1 = tk.Button(tp, text="opp1 ", command=tpo1)
tp1.grid(row=0, column=0)
tp2 = tk.Button(tp, text="opp2 ", command=tpo2)
tp2.grid(row=0, column=1)
tp3 = tk.Button(tp, text="opp3 ", command=tpo3)
tp3.grid(row=0, column=2)

to1 = tk.Label(tp, text="___")
to1.grid(row=1, column=0)
to2 = tk.Label(tp, text="___")
to2.grid(row=1, column=1)
to3 = tk.Label(tp, text="___")
to3.grid(row=1, column=2)

root.mainloop()
