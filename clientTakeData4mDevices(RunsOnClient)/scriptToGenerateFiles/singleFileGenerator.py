import random

fileN="2017-07-29.csv"
fp=open(fileN,"w")

fp.write("Time,Vac1,Vac2,Vac3,Vpv1,Vpv2,Iac1,Iac2,Iac3,Ipv1,Ipv2,Pnow,Etoday,Eall\n")
hour=9
minute=0
for row in range(1,600):
    fp.write(str(hour)+":"+str(minute)+",")
    for col in range(13):
        fp.write(str(random.randint(0,65535)))
        fp.write(",")
    minute=minute+1
    if minute >59:
        hour=hour+1
        minute=0
    
    fp.write(str(random.randint(0,65535)))
    fp.write("\n")
fp.close()


