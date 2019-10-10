from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()
scrollbar = Scrollbar(top, orient=VERTICAL)
Lb1 = Listbox(top,selectmode=BROWSE,yscrollcommand=scrollbar.set,width=5,height=1)



for d in range(1,31):
    Lb1.insert(d,str(d))
#Lb1.insert(1, "Python")
#Lb1.insert(2, "Perl")
#Lb1.insert(3, "C")
#Lb1.insert(4, "PHP")
#Lb1.insert(5, "JSP")
#Lb1.insert(6, "Ruby")
#Lb1.insert(7, "Python")
#Lb1.insert(8, "Perl")
#Lb1.insert(9, "C")
#Lb1.insert(10, "PHP")
#Lb1.insert(11, "JSP")
#Lb1.insert(12, "Ruby")
#Lb1.insert(13, "Python")
#Lb1.insert(14, "Perl")
#Lb1.insert(15, "C")
#Lb1.insert(16, "PHP")
#Lb1.insert(17, "JSP")
#Lb1.insert(18, "Ruby")

scrollbar.config(command=Lb1.yview)
scrollbar.pack(side=RIGHT, fill=Y)
#Lb1.yview_scroll ( 3, "units" )
Lb1.pack(side=LEFT, fill=BOTH, expand=0)
top.mainloop()
