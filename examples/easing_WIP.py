from easing_functions import *
import opc
import numpy as np
from time import sleep
import matplotlib.pyplot as plt

client = opc.Client('localhost:7890')

led_list = [(0,0,0)]*360           # list of 360 tuples, each containing R,G,B values.

a = BounceEaseInOut(start=3, end=1, duration=1)
b = BounceEaseIn(start=0, end=1)
c = BounceEaseOut(start=0, end=1)

x = np.arange(0, 1, 0.001)
y0 = list(map(a, x))
y1 = list(map(b, x))
y2 = list(map(c, x))

plt.plot(x,y0)
plt.plot(x,y1)
plt.plot(x,y2)

print(len(x))
plt.show()