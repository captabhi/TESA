import pickle as fp
from Tkinter import *
import matplotlib.pyplot as plt
import serial

myfile="logForModbus68.txt"
img="modbusDataplot2.png"

root =Tk()
canvas_width = 1000
canvas_height =1000




def plotLogImg():

    logFile=open(myfile,"r");
    global img
    plotList=[]
    registers=[]
    while 1:
    
        try:
            registers=fp.load(logFile)
            #print registers
            plotList.append(registers[0])
        
        except EOFError:
            break
    plt.plot(plotList,range(0,len(plotList)),'r')
    plt.savefig(img)
    logFile.close()


def butMagic():
    print "Hello Guys!"
    global img
    canvas = Canvas(None, 
                    width=canvas_width, 
                    height=canvas_height)
    canvas.pack()
    myimg = PhotoImage(file=img)
    canvas.create_image(20,20, anchor=NW, image=myimg)
    
def button1():
    global img
    novi = Toplevel()
    canvas = Canvas(novi, width =700, height = 500)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = img)
                                #image not visual
    canvas.create_image(50, 10, image = gif1, anchor = NW)
    #assigned the gif1 to the canvas object
    canvas.gif1 = gif1





plotLogImg()

but=Button(None,text="Press me",command=button1,height=20,width=30)
but.pack()
root.mainloop()
