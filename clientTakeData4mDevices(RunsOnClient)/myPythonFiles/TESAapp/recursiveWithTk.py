from Tkinter import *
import time

root=Tk()

v=IntVar()
v.set(0)
counter=0
def count(label):
    global counter
    counter = counter +1
    v.set(counter)
    time.sleep(0.1)
    print counter
    #label.config(text="Count is: "+str(v.get()))
    label.after(1000,count)
    


    

label=Label(root,height=10,width=20).pack()
count(label)
root.mainloop()
