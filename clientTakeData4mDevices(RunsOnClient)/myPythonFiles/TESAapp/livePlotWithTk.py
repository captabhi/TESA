import random
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import time
import Tkinter as tk


LARGE_FONT= ("Verdana", 12)
style.use("ggplot")


root=tk.Tk()
Xtick=[0,2,4,6,8,10,12,14,16]
Xticklabels=["Zero","One","Two","Three","Four","Five","Six"]

f = Figure(figsize=(5,5), dpi=100)
#f.add_axes([0,100,0,100])
a = f.add_subplot(111,xlabel="Time -->",ylabel="Pnow",ybound=100,xticks=Xtick,xticklabels=Xticklabels)

xList = []
yList = []
    

def animate():
    x=random.randint(0,20)
    y=random.randint(0,20)
    print "hello"
    #pullData = open("sampleText.txt","r").read()
    #dataList = pullData.split('\n')
    #for eachLine in dataList:
    #    if len(eachLine) > 1:
    #        x, y = eachLine.split(',')
    xList.append(int(x))
    yList.append(int(y))
    f.canvas.draw()
    f.config()
    #a.clear()
    a.plot(xList, yList)


            
#tp=tk.Toplevel(root)
canvas = FigureCanvasTkAgg(f,master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
toolbar = NavigationToolbar2TkAgg(canvas,root)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


#ani = animation.FuncAnimation(f, animate, interval=1000)
while True:
    root.update_idletasks()
    root.update()
    animate()
    
    time.sleep(1)
#root.mainloop()
