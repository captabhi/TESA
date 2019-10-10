from Tkinter import *

root = Tk()

root.wm_title("Kiosk")
root.geometry("300x75")
root.resizable(0, 0)

popcorn = Spinbox(root, from_=0, to=10, state="readonly")
popcorn.pack()

def getvalue():
    print(int(popcorn.get())*9)

button = Button(root, text="Get value", command=getvalue)
button.pack()


root.mainloop()  
