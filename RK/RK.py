import numpy as np
import matplotlib.pyplot as plt
import math
import random

def f(x, u1, u2, num):
    a = 3
    b = 4
    if num == 1:
        return u2
    elif num == 2:
        return -a*u2+b*math.sin(u1)

def rk4ForSyst(x, u1, u2, h):
    k11 = f(x, u1, u2, 1)
    k12 = f(x, u1, u2, 2)

    k21 = f(x + 0.5 * h, u1 + 0.5 * h * k11, u2 + 0.5 * h * k12, 1)
    k22 = f(x + 0.5 * h, u1 + 0.5 * h * k11, u2 + 0.5 * h * k12, 2)

    k31 = f(x + 0.5 * h, u1 + 0.5 * h * k21, u2 + 0.5 * h * k22, 1)
    k32 = f(x + 0.5 * h, u1 + 0.5 * h * k21, u2 + 0.5 * h * k22, 2)

    k41 = f(x + 0.5 * h, u1 + 0.5 * h * k31, u2 + 0.5 * h * k32, 1)
    k42 = f(x + 0.5 * h, u1 + 0.5 * h * k31, u2 + 0.5 * h * k32, 2)

    x = x + h
    v1 = u1 + h * (k11 + 2*(k21 + k31) + k41)/6
    v2 = u2 + h * (k12 + 2*(k22 + k32) + k42)/6
    return x,v1,v2

def rk4ForSystWithDblHop(x, u1, u2, h):
    x,v1,v2 = rk4ForSyst(x,u1,u2, 0.5*h)
    x,v1,v2 = rk4ForSyst(x,u1,u2, 0.5*h)
    return x,v1,v2

#def correctHop(u1,w1, e):
#    s = (w1 - u1)/(2**4 - 1)
#    lec = s * 2**4
#    if e/2**5 <= abs(s) and abs(s)>=e:
#        return lec, 0
#    elif abs(s) <= e/2**5:
#        return lec, 1
#    elif abs(s) > e:
#        return lec, 2

    

x= x1 = 0
u1 = w1 = 1
u2 = w2 = 1
h = 0.1
e = 0.001

xO = []
xO.append(x)
yO = []
yO.append(u1)
zO = []
zO.append(u2)
n = 500
c11 = c12 = c21 = c22 = 0
j = k = 0
lec1 = lec2 = 0
for i in range(0, n):
    x, u1, u2 = rk4ForSyst(x, u1, u2, h)
    x1, w1, w2 = rk4ForSystWithDblHop(x1, w1, w2, h)

    print("(xi:",x," v(1)i:",u1," v(2)i:",u2," w(1)i", w1," w(2)i", w2," u(1)i-w(1)i:", u1-w1," u(2)i-w(2)i:",u2-w2,")")
    xO.append(x)
    yO.append(u1)
    zO.append(u2)


plt.subplot(1,3,1)  
plt.plot(xO,yO,'r') # x, u ось

plt.subplot(1,3,2)
plt.plot(xO,zO,'r') # x, u' ось

plt.subplot(1,3,3)
plt.plot(yO,zO,'r') # фазовое пространство

plt.show()