import numpy as np
import matplotlib.pyplot as plt
import math
import random


def f(x, u, n, u1 = 0, temp = 0):             # функцию выбираю (изза этого приходится из функции в функцию тоскать n 
                                              # (это бы по хорошему  исправить, а то костыль какойто))
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    if n == '1' :
        return  u       
    elif n == '2':
        return  x/(1 + x**2) * u**2 + u - u**3 * math.sin(10*x)
    elif n == '3':
        if temp == 1: # f1:
            return u1
        elif temp == 2: # f2:
            return -a*u1-b*math.sin(u)
    else:
        return "vi eblan"



def correctHop(x, u, h, n, e):          # функцию корректирует шаг
    x1,v1 = rk4(x,u,h, n)
    x1,temp = rk4(x,u,0.5 * h, n)
    x1, v2 = rk4(x1, temp, 0.5 * h, n)
    s = (v2-v1)/(2**4 - 1)

    if abs(s)>=e/(2**5) and abs(s)<e:
       return h
    elif abs(s)>e:
       return h/2
    elif abs(s)<e:
        return 2*h




def rk4(x, u, h , n):
   
    x1 = x + h
    k1 = f(x,u, n)
    k2 = f(x + 0.5 * h,u + 0.5 * h * k1, n)
    k3 = f(x + 0.5 * h,u + 0.5 * h * k2, n)
    k4 = f(x + 0.5 * h,u + 0.5 * h * k3, n)
    u1 = u + h * (k1 + 2 * (k2 + k3) + k4) / 6
    return x1, u1

def rk4CorrHop(x, u, h , n, e):             #рунге кутт с ккорректировкой шага
   

    x1 = x + correctHop(x, u, h, n, e)


    k1 = f(x,u,n)
    k2 = f(x + 0.5 * correctHop(x, u, h, n, e),u + 0.5 * correctHop(x, u, h, n, e) * k1, n)
    k3 = f(x + 0.5 * correctHop(x, u, h, n, e),u + 0.5 * correctHop(x, u, h, n, e) * k2, n)
    k4 = f(x + 0.5 * correctHop(x, u, h, n, e),u + 0.5 * correctHop(x, u, h, n, e) * k3, n)
    u1 = u + correctHop(x, u, h, n, e) * (k1 + 2 * (k2 + k3) + k4) / 6
    return x1, u1

def rk4ForSyst(x, u, h , n, u1):
   
    x1 = x + h
    k11 = f(x,u, n , u1,1)
    k12 = f(x,u, n , u1,2)

    k21 = f(x + 0.5 * h,u + 0.5 * h * k11, n, u1, 1)
    k22 = f(x + 0.5 * h,u + 0.5 * h * k12, n, u1, 2)

    k31 = f(x + 0.5 * h,u + 0.5 * h * k21, n, u1,1)
    k32 = f(x + 0.5 * h,u + 0.5 * h * k22, n, u1,2)

    k41 = f(x + 0.5 * h,u + 0.5 * h * k31, n, u1,1)
    k42 = f(x + 0.5 * h,u + 0.5 * h * k32, n, u1,2)

    u = u + h * (k11 + 2 * (k21 + k31) + k41) / 6
    u1 = u1 + h * (k12 + 2 * (k22 + k32) + k42) / 6
    return x1, u, u1

print("Choose a task:")                         # типа менюшка
print("1) test: du/dx = u")
print("2)  du/dx = x/(1 + x**2) * u**2 + u - u**3 * sin(x)")
print("3) u'' + a*u' + b*sin(u)")
print("___________________________________________________________")
num = input()
temp = 1

if num == '1' :
    print("du/dx = u")  
    print("Without correct hop, enter '1' ")
    print("With correct hop, enter '2' ")
    temp = int(input())

    if temp == 2:
        print("input e, inaccuracy control parameter")
        e = float(input())
elif num == '2':
    print("du/dx = x/(1 + x**2) * u**2 + u - u**3 * sin(x)")
elif num == '3':
    print("3) u'' + a*u' + b*sin(u)")
    print("Input u': ")
    u1 = float(input())
    temp = 3
    y1O = [u1]
else:
    print("vi eblan")


x = 0
print("Input 'u' value: ")
u = float(input())
print("Input hop(h) value: ")
h = float(input())
print("hop count: ")
n = float(input())
i = 0
                    #менюшка закончилась

xO = [x]
yO = [u]

print("| x:", x,"\t","u:", u,"| ") # с этим я тоже чот объебался, и решил так вывести

while i < n:
    if temp == 1:
        x, u  = rk4(x, u, h, num)
        print(i+1,") ","| x:", x,"\t","u:", u,"| ") #тут бы значение округлить, а то не красиво получается
        xO.append(x)
        yO.append(u)
        i+=1
    elif temp == 2:
         x, u  = rk4CorrHop(x, u, h, num, e)
         print(i+1,") ","| x:", x,"\t","u:", u,"| ")
         xO.append(x)
         yO.append(u)
         i+=1
    elif temp == 3:
         x, u, u1 = rk4ForSyst(x, u, h, num, u1)
         print(i+1,") ","| x:", x,"\t","u:", u,"| ","\t","u1:", u1,"| ")
         xO.append(x)
         yO.append(u)
         y1O.append(u1)
         i+=1
   


y1 = np.array(yO)
x1 = np.array(xO)

if (temp == 1 or temp == 2) and num == '1' : 
    
    plt.plot(x1, np.e**x1,'b')  # точное решение (синий)
    plt.plot(x1,y1,'r')         # рунге кутт (красный)

elif temp == 1:
     plt.plot(x1,y1,'r')

elif temp == 3:
    u1 = np.array(y1O)
    plt.subplot(1,3,1)
    plt.plot(x1,y1,'r')

    plt.subplot(1,3,2)
    plt.plot(x1,u1,'r')

    plt.subplot(1,3,3)
    plt.plot(y1,u1,'r')

plt.show()