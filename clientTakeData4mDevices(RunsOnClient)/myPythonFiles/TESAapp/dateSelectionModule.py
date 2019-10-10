from Tkinter import *

master = Tk()
i=5
w = Spinbox(master, from_=0, to=10,disabledbackground="grey",textvariable=i,activebackground="blue")
w.pack()
print i
mainloop()
