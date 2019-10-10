from matplotlib.figure import Figure 
import random
import numpy as np
    
data=[]
i=0
xtick=[]
for j in range(7,20):
    xtick.append(str(j)+":"+"00")
    xtick.append(str(j)+":"+"30")
    
xtickBand=np.arange(420,20*60+30,30)

print xtick
fig = Figure(figsize=(10,10))
plt = fig.add_subplot(111)
plt.axis([420,20*60+30,0,65535])
#plt.xticks(xtickBand,xtick)
plt.grid(True)
#plt.tight_layout()
    
plt.ion()

xData=[]
while i<600:
    data.append(random.randint(0,65535))
    xData.append(420+i)
    plt.pause(0.05)
    
    plt.plot(xData,data)
    
    #plt.show()
    #plt.draw()
    i=i+1
    #plt.show()
plt.ioff()
plt.show()
