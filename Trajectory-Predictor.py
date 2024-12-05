import matplotlib.pyplot as plt
import numpy as np
import math
ang=int(input("What angle of launch?"))
vel=float(input("Speed of launch?"))
yvel=math.sin(math .radians(ang))*vel
xvel=math.cos(math.radians(ang))*vel
t=np.linspace(0, 100,num=1000)
y=yvel*t-(9.8*t**2)/2
x=xvel*t
timex=(-1*yvel-yvel)/-9.8
root=timex*xvel
height=yvel*(timex/2)-(9.8*(timex/2)**2)/2
heightx=(timex/2)*xvel
print("Launch angle:", ang)
print("Launch velocity:", vel,"m/s")
print("land at",root,"m")
print("The projectile reaches", height, "m after", height, "m")
plt.figure(num=0, dpi=120)
if height >= root:
    plt.ylim(0, height*1.05)
    plt.xlim(0,height+1.05)
else:
    plt.ylim(0, root*1.05)
    plt.xlim(0,root*1.05)
plt.plot(t,y, label="Y position//time")
plt.plot(t,x, label="X position/time")
plt.plot(x,y, label="Trajectory")
plt.plot(root,0,'o') 
plt.plot(heightx,height,"o")
plt.legend()
plt.show()