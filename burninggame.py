# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:34:23 2020

@author: Loïc Girard
"""

import time
import matplotlib.pyplot as plt
import burninggamedef as bgd
import tkinter as tk

"""

circle1=plt.Circle((0,-0.5),0.25,color='r')
circle2=plt.Circle((0,0.5),0.25,color='r')

rectangle1=plt.Rectangle((-0.5,0),1,1,fill=0)
blank1=plt.Rectangle((-0.5,0),0.99,0.99,color='w')

rectangle2=plt.Rectangle((-0.5,-1),1,1,fill=0)
blank2=plt.Rectangle((-0.5,-1),0.99,0.99,color='w')

fig,ax=plt.subplots()
plt.grid()
plt.xlim(-2,2)
plt.ylim(-2,2)



ax.add_artist(rectangle1)
ax.add_artist(rectangle2)
ax.add_artist(circle1)
plt.show()

for i in range(0,10):
    if i%2==0:
        ax.add_artist(circle1)
    else:
        ax.add_artist(circle2)
    plt.show()
    plt.pause(0.5)
    ax.add_artist(blank1)
    ax.add_artist(blank2)
    plt.show()
    plt.pause(0.25)
"""

i=-1
k=0
side=0
t=0
y=0
yb=315
cs=1
g=1
n=1

game=tk.Tk()

def ChangePos(evt):
    global i,yb
    i=i+1
    if i%2==0:
        yb=65
        w.delete('c2')
        w.create_oval(665,yb,835,235,fill='red',tags='c1')
    else:
        yb=315
        w.delete('c1')
        w.create_oval(665,yb, 835, 485,fill='red',tags='c2')


def delete_frame():
    for widget in game.winfo_children():
        widget.destroy()
        print('Restrating')
    

    
while(1==1):
    if (n==1):
        w=tk.Canvas(game,width=1500, height=1000)
        w.pack()

        w.create_rectangle(625, 25, 875, 275,fill='white')
        w.create_rectangle(625, 275, 875, 525,fill='white')

        w.create_oval(665, 315, 835, 485,fill='red',tags='c2')
        g=1
    
    while(g==1):
        t+=1
        w.bind('<Button-1>',ChangePos)
        if (t%2==0):
            x=1265-t*25
            y=315-k*250
            w.delete('c3')
            w.create_rectangle(x,y, 1435-t*25, 485-k*250,fill='blue',tags='c3')
        if (t%20==0):
            k=not(k)
            t=0
        w.update()
        time.sleep(0.25)
        if (y==yb and x<835):
            delete_frame()            
            time.sleep(1)
            g=0
            n=0
            game.update()
    n+=1


