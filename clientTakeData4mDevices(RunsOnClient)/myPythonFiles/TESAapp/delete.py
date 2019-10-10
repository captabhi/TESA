from Tkinter import *

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()

fr=Frame(master)
fr.pack()
frame=Toplevel(fr)

Label(frame, text="First Name").grid(row=0)
Label(frame, text="Last Name").grid(row=1)

e1 = Entry(frame)
e2 = Entry(frame)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(frame, text='Quit', command=frame.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(frame, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
