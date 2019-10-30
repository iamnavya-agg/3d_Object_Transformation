# CSE 101 - IP HW4
# Disc(part-1) 
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
    return [result[0],result[1]]


def scale(x,y,r,a,b,h,k):
    #Function to scale the x and y radius of disc using matrix multiplication 
    matrix = [[h,0,0],[0,k,0],[0,0,1]]
    old1 = r[0]
    old2 = r[1]
    r=multiply(matrix,[r[0],r[1],1])
    for i in range(202):
        x[i] = x[i]/old1*r[0]
        y[i] = y[i]/old2*r[1]
    return r


def rotate(x,y,r,angle):
    #Function to rotate the disc by an angle thetha using matrix multiplication
    from math import sin,cos,radians,ceil,floor
    matrix = [[cos(radians(angle)),(-1*sin(radians(angle))),0],[sin(radians(angle)),cos(radians(angle)),0],[0,0,1]]
    r[0],r[1] = multiply(matrix,[r[0],r[1],1])
    for i in range(202):
        x[i],y[i] = multiply(matrix,[x[i],y[i],1])
    return r


def translate(x,y,ab,x_mov,y_mov):
    #Function to change the centre of disc using matrix multiplication
    matrix = [[1,0,x_mov],[0,1,y_mov],[0,0,1]]
    for i in range(202):
        x[i],y[i] = multiply(matrix,[x[i],y[i],1])
    ab[0],ab[1] = multiply(matrix,[ab[0],ab[1],1])
    return ab


def regulate(x,y,a,b,r1,r2):
    #Function wth loop used for re-transformation over the disk
    plt.plot(x,y)           #Using plot from matplotlib to plot the disk
    r = [r1,r2]
    while(True):
        option = input().split()
        if option[0] == "S":
            r = scale(x,y,r,a,b,float(option[1]),float(option[2]))
            print(a,b,*r)
        elif option[0] == "R":
            r = rotate(x,y,r,float(option[1]))
            for i in range(len(r)):
                r[i] = round(r[i],2)
            print(a,b,*r)
        elif option[0] == "T":
            ab = [a,b]
            ab = translate(x,y,ab,float(option[1]),float(option[2]))
            print(*ab,*r)
        else:
            break
        #plt.gcf().clear()          # Function to clear screen after one transformation( Commented to observe change in figure)
        plt.plot(x,y)


            
def main_func():
    a,b,r = map(int,input().split())
    x,y=[],[]
    from math import sin,cos,pi
    for i in range(201):
        x.append(round(r*cos(i*2*pi/200),5)+a)
        y.append(round(r*sin(i*2*pi/200),5)+b)
    x.append(x[0])
    y.append(y[0])
    regulate(x,y,a,b,r,r)
