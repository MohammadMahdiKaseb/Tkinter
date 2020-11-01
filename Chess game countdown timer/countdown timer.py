import tkinter as tk
from threading import Thread
from time import sleep


##################################################################################################################
def stop(side):                                                                                                  #
    global flag                                                                                                  #
    if side == 'left':                                                                                           #
        flag = True                                                                                              #
    else:                                                                                                        #
        flag = False



def begin():
    value = int(time_value.get())
    m, s = divmod(value, 60)
    r_timer.set('%02d:%02d' % (m, s))
    l_timer.set('%02d:%02d' % (m, s))
    thread1 = Thread(target=start, args=(value,))  #
    thread1.start()

##################################################################################################################
def start(val):                                                                                                    #
    timer["left"] = timer["right"] = val
    while True:                                                                                                  #
        if timer["left"] == 0 or timer["right"] == 0:
           break
        sleep(1)                                                                                                 #
        if flag:                                                                                                 #
            timer['right'] -= 1                                                                                  #
            m, s = divmod(timer['right'], 60)                                                                    #
                                                                                                                 #
            r_timer.set('%02d:%02d' % (m, s))                                                                    #
        else:                                                                                                    #
            timer['left'] -= 1                                                                                   #
            m, s = divmod(timer['left'], 60)                                                                     #                                                                                                     #
            l_timer.set('%02d:%02d' % (m, s))                                                                    #
##################################################################################################################
l_cnf = {'bg': '#2f3640', 'fg': '#e84118'}
tk_cnf = {'bg': "#2f3542"}
lr_cnf = {"bg" : "#fbc531"}
b_cnf = {'bg': '#c7ecee',
         'activebackground': '#1e90ff',
         'highlightbackground': '#e55039'}
##################################################################################################################
root = tk.Tk()                                                                                                   #
root.resizable(0, 0)
root.title('꓄ꊛꊩ')
root.config(cnf=tk_cnf)


##################################################################################################################
timer = {}                                                                                          #
flag = False                                                                                                     #
#########TIMER##########                                                                                         #
l_timer = tk.StringVar()                                                                                         #
l_timer.set("00:00")                                                                                             #
r_timer = tk.StringVar()                                                                                         #
r_timer.set("00:00")                                                                                             #
##################################################################################################################
tk.Label(root, text="Left player",cnf=lr_cnf, font=("times", 15,)).grid(row=0, column=0)                                    #
tk.Label(root, text="Right player",cnf=lr_cnf, font=("times", 15,)).grid(row=0, column=1, sticky=tk.N + tk.E)               #
##################################################################################################################
tk.Label(root,cnf=l_cnf, textvariable=l_timer).grid(row=1, column=0)                                                       #
                                                                                                                 #
tk.Label(root,cnf=l_cnf, textvariable=r_timer).grid(row=1, column=1)                                                       #
##################################################################################################################
tk.Button(root,cnf=b_cnf, text="Stop",command=lambda: stop('left'), font=("times", 15,)).grid(row=2, column=0)  #
tk.Button(root,cnf=b_cnf, text="Stop",command=lambda: stop('right'), font=("times", 15,)).grid(row=2, column=1)#
tk.Button(root, cnf=b_cnf, text="Start", command= begin, font=("times", 15,)).grid(row=4, column=0, columnspan = 2,sticky=tk.W+tk.E)                                                                                                           #
tk.Button(root, cnf=b_cnf, text="Cancel", command= root.destroy, font=("times", 15,)).grid(row=5, column=0, columnspan = 2
,sticky=tk.W+tk.E)
time_value = tk.StringVar()
tk.Entry(root,textvariable=time_value,
         font=("times", 15,)).grid(row=3, column=0 , columnspan = 2 , sticky=tk.W+tk.E)
##################################################################################################################
                                                                                                                 #
                                                                                                #
                                                                                                                 #
root.mainloop()                                                                                                  #
##################################################################################################################