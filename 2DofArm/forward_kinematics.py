# -*- coding: utf-8 -*-
import numpy as np
from numpy import sin,cos
import matplotlib.pyplot as plt

def fk(l1, l2, th1, th2):
    x2 = l1 * cos(th1) + l2 * cos(th2)
    y2 = l1 * sin(th1) + l2 * sin(th2)

    x1 = l1 * cos(th1)
    y1 = l1 * sin(th1)

    return x1, y1, x2, y2

def plot(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # draw link
    plt.plot(x, y,"-b",lw=5, label="link")
    # draw joint
    plt.plot(x, y,"or",lw=5, ms=10, label="joint")
    # set limit
    plt.xlim(-0.4, 0.4)
    plt.ylim(-0.1,0.4)
    plt.grid()
    plt.show()
    
def run():
    # the length of link
    l1, l2 = 0.18, 0.16

    # the angular of link
    [th1, th2] = np.radians([45, -15])

    # calcurate the fk
    x1, y1, x2, y2 = fk(l1, l2, th1, th2)
    
    # store the position to x,y list 
    x = [0, x1, x2]
    y = [0, y1, y2]

    # plot 2dof robot arm
    plot(x, y)

if __name__ == '__main__':
    run()
