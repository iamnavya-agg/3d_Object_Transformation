# CSE 101 - IP HW4
# Polygon(part-2)
# Name: Navya Aggarwal
# Roll Number: 2018349
# Section: B
# Group: 6
# Date: 20 November 2018


import matplotlib.pyplot as plt
plt.ion()


def multiply(x,y):
    #Function to perform matrix multipication of 3*3 and 1*3 matrices and return the first two elements of the new matrix
    result=[0,0,0]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i]+=x[i][j]*y[j]
    return result[0],result[1]


def scale(x,y,a,b):
    #Function to scale the x and y coordinates of polygon using matrix multiplication
    matrix = [[a,0,0],[0,b,0],[0,0,1]]
    for i in range(len(x)):
        x[i],y[i]=multiply(matrix,[x[i],y[i],1])



def rotate(x,y,angle):
    #Function to rotate the polygon by an angle thetha using matrix multiplication
    from math import sin,cos,radians,ceil,floor
    matrix = [[cos(radians(angle)),(-1*sin(radians(angle))),0],[sin(radians(angle)),cos(radians(angle)),0],[0,0,1]]
    for i in range(len(x)):
        x[i],y[i]=multiply(matrix,[x[i],y[i],1])



def translate(x,y,a,b):
    #Function to change the coordinates of polygon using matrix multiplication
    matrix = [[1,0,a],[0,1,b],[0,0,1]]
    for i in range(len(x)):
        x[i],y[i]=multiply(matrix,[x[i],y[i],1])
    


def regulate(x,y):
    #Function wth loop used for re-transformation over the ploygon
    plt.plot(x,y)               #Using plot from matplotlib to plot the polygon
    while(True):
        option = input().split()
        if option[0] == "S":
            scale(x,y,float(option[1]),float(option[2]))
        elif option[0] == "R":
            rotate(x,y,float(option[1]))
            for i in range(len(x)):
                x[i] = round(x[i],2)
                y[i] = round(y[i],2)
        elif option[0] == "T":
            translate(x,y,float(option[1]),float(option[2]))
        else:
            break
        #plt.gcf().clear()                  # Function to clear screen after one transformation( Commented to observe change in figure)
        plt.plot(x,y)
        print(*x[:-1])
        print(*y[:-1])

def main_func():
    x = list(map(int,input().split(" ")))
    y = list(map(int,input().split(" ")))
    x.append(x[0])
    y.append(y[0])
    regulate(x,y)
