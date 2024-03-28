import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.animation import FuncAnimation
import sympy as sp
def hipocicloid(t, r, R):
    x = (R - r) * np.cos(t) + r * np.cos((R - r) / r * t)
    y = (R - r) * np.sin(t) - r * np.sin((R - r) / r * t)
    return x, y
def epicicloid(t, r, R):
    x = (R + r) * np.cos(t) - r * np.cos((R + r) / r * t)
    y = (R + r) * np.sin(t) - r * np.sin((R + r) / r * t)
    return x, y
def cicloid(t, r):
    x = r*(t-np.sin(t))
    y = r*(1-np.cos(t))
    return x, y
def value(wartosc_x, function):
    x = sp.symbols('x')
    return function.subs(x, wartosc_x)

def G2(x):
    return (14*x *np.exp(-8*x))/(10**6*(4*x+13*np.exp(x)))

def dG2(x):
    return np.exp(-8*x)*(-224*x**2-91*np.exp(x)*(-1+9*x))/(500000*(13*np.exp(x)+4*x)**2)
def function(t,r):
    x = r * (t - np.sin(t)+np.sin(t))
    y = r * (1 - np.cos(t))+G2(t)*r*np.cos(t)
    return x,y
def update(num, t, r, R,line, circle_small, connecting_line):
    if trochoid_type == "hipocycloid":
        x, y = hipocicloid(t[:num], r, R)
        circle_small.center = ((R - r) * np.cos(t[num]), (R - r) * np.sin(t[num]))
        connecting_line.set_data([(R - r) * np.cos(t[num]) + r * np.cos((R - r) / r * t[num]), circle_small.center[0]], [(R - r) * np.sin(t[num]) - r * np.sin((R - r) / r * t[num]), circle_small.center[1]])
        line.set_data(x, y)
    elif trochoid_type == "epicycloid":
        x, y = epicicloid(t[:num], r, R)
        circle_small.center = ((R + r) * np.cos(t[num]), (R + r) * np.sin(t[num]))
        connecting_line.set_data([(R + r) * np.cos(t[num]) - r * np.cos((R + r) / r * t[num]), circle_small.center[0]], [(R + r) * np.sin(t[num]) - r * np.sin((R + r) / r * t[num]), circle_small.center[1]])
        line.set_data(x, y)
    elif trochoid_type == "cycloid":
        x,y = cicloid(t[:num], r)
        circle_small.center = (r * (t[num]), r)
        connecting_line.set_data([r*(t[num]-np.sin(t[num])), circle_small.center[0]], [r*(1-np.cos(t[num])), circle_small.center[1]])
        line.set_data(x, y)
    elif trochoid_type == "function":
        x, y = cicloid(t[:num], r)
        circle_small.center = (r * (t[num]), r)
        connecting_line.set_data([r * (t[num] - np.sin(t[num])), circle_small.center[0]],
                                 [r * (1 - np.cos(t[num])), circle_small.center[1]])
        line.set_data(x, y)
    return line, circle_small, connecting_line

if __name__ == "__main__":
    fig, ax = plt.subplots()
    R = 0
    trochoid_type = input("Enter trochoid type (cycloid, hipocycloid, epicycloid, function): ")
    if trochoid_type == "function":
        t = np.linspace(-2, -1, 1000)
        r = float(input("Enter the value of r: "))
        line, = ax.plot([], [], label=f'{trochoid_type} (r={r}')
    else:
        t = np.linspace(0, 6 * np.pi, 1000)

    if trochoid_type == "cycloid":
        r = float(input("Enter the value of r: "))
        line, = ax.plot([], [], label=f'{trochoid_type} (r={r}')

    elif trochoid_type == "hipocycloid" or trochoid_type == "epicycloid":
        while(True):
            print("Remember that R/r must be a rational number!")
            R = float(input("Enter the value of R: "))
            r = float(input("Enter the value of r: "))
            line, = ax.plot([], [], label=f'{trochoid_type} (r={r}, R={R}')

            if R % r == 0:
                break
            else:
                continue

    if trochoid_type == "hipocycloid" or trochoid_type == "epicycloid":
        circle = plt.Circle((0, 0), R, color='black', fill=False, linestyle='-', linewidth=2)
        plt.gca().add_patch(circle)
    elif trochoid_type == "cycloid":
        plt.axhline(0, color='black', linestyle='-', linewidth=2)
    elif trochoid_type == "function":
        plt.xlim(-2, -1)
        plt.ylim(-10, 10)
        y = G2(t)
        plt.plot(t,y)
    circle_small = plt.Circle((0, 0), r, color='black', fill=False, linestyle='-', linewidth=2)
    ax.add_patch(circle_small)
    connecting_line, = ax.plot([], [], color='red', linestyle='--', linewidth=2)
    ax.axis('equal')


    if trochoid_type == "hipocycloid" or trochoid_type == "epicycloid":
        ax.set_xlim([-(R + r) * 1.5, (R + r) * 1.5])
        ax.set_ylim([-(R + r) * 1.5, (R + r) * 1.5])
    elif trochoid_type == "cycloid":
        ax.set_xlim([-2*r, (2*r)*2*r])
        ax.set_ylim([-(2*r)*2, (2*r) * 2])

    ani = FuncAnimation(fig, update, frames=len(t), fargs=(t, r, R, line, circle_small, connecting_line),
                        interval=50)

    plt.show()

