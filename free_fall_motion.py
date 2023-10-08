import numpy as np
import matplotlib.pyplot as plt

vi=20		#m/s
h=30		#m
g=9.8		#m/s/s
t= np.linspace(0,2,100)

ym=h-1/2*g*t**2
yh=vi*t-1/2*g*t**2

plt.grid()
plt.xlabel("time(s)")
plt.ylabel("Hight(m)")
plt.plot(t, ym)
plt.plot(t, yh)
plt.show()

