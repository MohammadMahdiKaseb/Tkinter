import tkinter as tk

root = tk.Tk()

l1 = tk.Label(root, text="LL1", bg="green")
l1.grid(row=0, column=0, rowspan=3, sticky=tk.S + tk.N)

l2 = tk.Label(root, text="LL2", bg="red")
l2.grid(row=0, column=1, columnspan=3, sticky=tk.W + tk.E)

l3 = tk.Label(root, text="LL3", bg="blue")
l3.grid(row=1, column=1, rowspan=2, sticky=tk.S + tk.N)

l4 = tk.Label(root, text="LL4", bg="pink")
l4.grid(row=1, column=2, rowspan=2, sticky=tk.S + tk.N)

l5 = tk.Label(root, text="LL5", bg="blue")
l5.grid(row=1, column=3)

l6 = tk.Label(root, text="LL6", bg="yellow")
l6.grid(row=3, column=3)

root.mainloop()
