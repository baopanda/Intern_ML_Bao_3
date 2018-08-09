import matplotlib.pyplot as plt
from numpy import *

x = linspace(0,10,1000)
# print(x)
f = (pow(e,(-x/10)))*sin(pi*x)
g = x*pow(e,(-x/3))
plt.plot(x, f,label="f(x) = (e^(−x/10))*sin(πx)")
plt.plot(x,g, label="g(x) = x*e^(−x/3)")
plt.legend(loc=0)
plt.show()