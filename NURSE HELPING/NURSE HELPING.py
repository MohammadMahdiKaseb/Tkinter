import tkinter as tk
from tkinter import Button
import tkinter.ttk as ttk
from time import sleep  
from threading import Thread


def time_format(seconds):
    h  = int(seconds / 3600)
    temp = seconds % 3600
    m = temp / 60
    s = temp % 60
    return "%02d:%02d:%02d:"%(h ,m ,s)

def counter(seconds ,var , button ):
    button.config(state = tk.DISABLED)
    while seconds:
        sleep(1)
        seconds -= 1
        var.set(time_format(seconds))
    button.config(state = tk.ACTIVE)
def callback(arg1 , arg2 ,arg3):
    p1.set(e1.get())

def callback2(arg1 , arg2 ,arg3):
    p2.set(e2.get())
def callback3(arg1 , arg2 ,arg3):
    p3.set(e3.get())
def callback_t1(arg1 , arg2 ,arg3):
    l1.set("%02d:%02d:%02d"%(int(h_p_1.get()),int(m_p_1.get()),int(s_p_1.get())))
def callback_t2(arg1 , arg2 ,arg3):
    l2.set("%02d:%02d:%02d"%(int(h_p_2.get()),int(m_p_2.get()),int(s_p_2.get())))
def callback_t3(arg1 , arg2 ,arg3):
    l3.set("%02d:%02d:%02d"%(int(h_p_3.get()),int(m_p_3.get()),int(s_p_3.get())))                  
def start(number):
    if number == 1 :
        seconds1 = int(h_p_1.get()) * 3600 + int(m_p_1.get()) * 60 + int(s_p_1.get())
        th1 = Thread(target = counter , args = (seconds1 , l1, b1))
        th1.start()
    elif number == 2 :
        seconds2 = int(h_p_2.get()) * 3600 + int(m_p_2.get()) * 60 + int(s_p_2.get())
        th1 = Thread(target = counter , args = (seconds2 , l2 , b2))
        th1.start()
    else :
        seconds3 = int(h_p_3.get()) * 3600 + int(m_p_3.get()) * 60 + int(s_p_3.get())
        th1 = Thread(target = counter , args = (seconds3 , l3, b3))
        th1.start()


root = tk.Tk()
root.title("(NURSE HELPING)-TIX")
note = ttk.Notebook()
note.grid(row=0, column=0)

timer = tk.Frame()
patient = tk.Frame()

note.add(timer, text='Timer')
note.add(patient, text='Patient')

# ############### Timer First Row ############## #
p1 = tk.StringVar()
p1.set('T1')
tk.Label(timer, textvariable=p1).grid(row=0, column=0)
p2 = tk.StringVar()
p2.set('T2')
tk.Label(timer, textvariable=p2).grid(row=0, column=1)
p3 = tk.StringVar()
p3.set('T3')
tk.Label(timer, textvariable=p3).grid(row=0, column=2)
# ############### Timer First Row ############## #
l1 = tk.StringVar()
l1.set('00:00:00')
tk.Label(timer, textvariable=l1).grid(row=1, column=0)
l2 = tk.StringVar()
l2.set('00:00:00')
tk.Label(timer, textvariable=l2).grid(row=1, column=1)
l3 = tk.StringVar()
l3.set('00:00:00')
tk.Label(timer, textvariable=l3).grid(row=1, column=2)
# ############### Butten ############## #
b1 = tk.Button(timer , text = "START" , command = lambda : start(1) )
b1.grid(row = 2 , column = 0)
b2 = tk.Button(timer , text = "START" , command = lambda : start(2) )
b2.grid(row = 2 , column = 1)
b3 = tk.Button(timer , text = "START" , command = lambda : start(3) )
b3.grid(row = 2 , column = 2)
tk.Button(timer , text = "CANCEL" , command = root.destroy  ).grid(row = 3 , column = 0 , columnspan = 3
 , sticky = tk.W+tk.E )
###########################################
patient1 = tk.LabelFrame(patient , text='Patient1')
patient1.grid(row = 0 , column = 0 , padx=10)

tk.Label(patient1, text = "NAME:").grid(row=0, column=0)
tk.Label(patient1, text = "TIME:").grid(row=1, column=0)
patient2 = tk.LabelFrame(patient , text='Patient2')
patient2.grid(row = 1 , column = 0 , padx=10)

tk.Label(patient2, text = "NAME:").grid(row=0, column=0)
tk.Label(patient2, text = "TIME:").grid(row=1, column=0)
patient3 = tk.LabelFrame(patient , text='Patient3')
patient3.grid(row = 2 , column = 0 , padx=10)

tk.Label(patient3, text = "NAME:").grid(row=0, column=0)
tk.Label(patient3, text = "TIME:").grid(row=1, column=0)

##
h_p_1 = tk.StringVar()
h_p_1.set("00")
m_p_1 = tk.StringVar()
m_p_1.set("00")
s_p_1 = tk.StringVar()
s_p_1.set("00")
f1 = tk.Frame(patient1)
f1.grid(row= 1 , column = 1)
tk.Spinbox(f1 ,
 from_ = 0 ,
  to = 23 ,
   wrap = True ,
    textvariable = h_p_1 ,
     width = 2 , 
     state = "readonly").grid(row = 0 , column = 0)
tk.Spinbox(f1 ,
 from_ = 0 ,
  to = 59 ,
   wrap = True ,
    textvariable = m_p_1 ,
     width = 2 , 
     state = "readonly").grid(row = 0 , column = 1)
tk.Spinbox(f1 ,
 from_ = 0 ,
  to = 59 ,
   wrap = True ,
    textvariable = s_p_1 ,
     width = 2 , 
     state = "readonly").grid(row = 0 , column = 2)
h_p_2 = tk.StringVar()
h_p_2.set("00")
m_p_2 = tk.StringVar()
m_p_2.set("00")
s_p_2 = tk.StringVar()
s_p_2.set("00")
f2 = tk.Frame(patient2)
f2.grid(row= 1 , column = 1)
tk.Spinbox(f2 ,
 from_ = 0 ,
  to = 23 ,
   wrap = True ,
    textvariable = h_p_2 ,
     width = 2 , 
     state = "readonly").grid(row = 0 , column = 0)
tk.Spinbox(f2 ,
 from_ = 0 ,
  to = 59 ,
   wrap = True ,
    textvariable = m_p_2 ,
     width = 2 , 
     state = "readonly").grid(row = 0 , column = 1)
tk.Spinbox(f2 ,
 from_ = 0 ,
  to = 59 ,
   wrap = True ,
    textvariable = s_p_2 ,
     width = 2 , 
     state = "readonly").grid(row = 0 , column = 2)     
h_p_3 = tk.StringVar()
h_p_3.set("00")
m_p_3 = tk.StringVar()
m_p_3.set("00")
s_p_3 = tk.StringVar()
s_p_3.set("00")
f3 = tk.Frame(patient3)
f3.grid(row= 1 , column = 1)
tk.Spinbox(f3 ,
 from_ = 0 ,
    to = 23 ,
    wrap = True ,
    textvariable = h_p_3 ,
    width = 2 , 
    state = "readonly").grid(row = 0 , column = 0)
tk.Spinbox(f3 ,
    from_ = 0 ,
    to = 59 ,
    wrap = True ,
    textvariable = m_p_3 ,
    width = 2 , 
    state = "readonly").grid(row = 0 , column = 1)
tk.Spinbox(f3 ,
 from_ = 0 ,
  to = 59 ,
   wrap = True ,
    textvariable = s_p_3 ,
     width = 2 , 
     state = "readonly").grid(row = 0 , column = 2)          
e1 = tk.StringVar()
e1.trace("w" , callback)
e2 = tk.StringVar()
e2.trace("w" , callback2)
e3 = tk.StringVar()
e3.trace("w" , callback3)



tk.Entry(patient1 ,textvariable = e1 ).grid(row = 0 , column = 1)

tk.Entry(patient2 ,textvariable = e2 ).grid(row = 0 , column = 1)

tk.Entry(patient3 ,textvariable = e3 ).grid(row = 0 , column = 1)


# #############-TIMER CALBAKS-############ #

h_p_1.trace("w" , callback_t1)
m_p_1.trace("w" , callback_t1)
s_p_1.trace("w" , callback_t1)
h_p_2.trace("w" , callback_t2)
m_p_2.trace("w" , callback_t2)
s_p_2.trace("w" , callback_t2)
h_p_3.trace("w" , callback_t3)
m_p_3.trace("w" , callback_t3)
s_p_3.trace("w" , callback_t3)



root.mainloop()