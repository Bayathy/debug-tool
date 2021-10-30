from matplotlib.colors import to_rgba_array
import numpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import tkinter as tk
import random

from numpy.lib.function_base import angle

x_data=[1,4,5,2,5,7,5,2,4,6]
y_data=[2,5,1,3,5,4,1,3,6,2]
x_line=[0,0,0]
y_line=[0,0,0]


def set_label():
    label1['text'] = "x:" + str(x_data[0]) + " "+ "y:" + str(y_data[0])
    label2['text'] = "x:" + str(x_data[1]) + " "+ "y:" + str(y_data[1])
    label3['text'] = "x:" + str(x_data[2]) + " "+ "y:" + str(y_data[2])
    label4['text'] = "x:" + str(x_data[3]) + " "+ "y:" + str(y_data[3])
    label5['text'] = "x:" + str(x_data[4]) + " "+ "y:" + str(y_data[4])
    label6['text'] = "x:" + str(x_data[5]) + " "+ "y:" + str(y_data[5])
    label7['text'] = "x:" + str(x_data[6]) + " "+ "y:" + str(y_data[6])
    label8['text'] = "x:" + str(x_data[7]) + " "+ "y:" + str(y_data[7])
    label9['text'] = "x:" + str(x_data[8]) + " "+ "y:" + str(y_data[8])
    label10['text'] = "x:" + str(x_data[9]) + " "+ "y:" + str(y_data[9])

def rotate_laser(angle,frame):
    for i in range(10):
        dx = laser_x[i][1] - 4 + rcl[i]
        dy = laser_y[i][1] - 4
       
        laser_replace[i][0] = rcl[i] * numpy.cos(angle * numpy.pi/180)
        laser_replace[i][1] = rcl[i] * numpy.sin(angle * numpy.pi/180)

        #laser_x[i][0] += laser_replace[i][0] 
        

        laser_rotate[i][0] = dx * numpy.cos(angle * numpy.pi/180) - dy * numpy.sin(angle * numpy.pi/180) + 4
        laser_rotate[i][1] = dx * numpy.sin(angle * numpy.pi/180) + dy * numpy.cos(angle * numpy.pi/180) + 4

    #dx = laser_x[0][1] - x_data[frame]
    #dy = laser_y[0][1] - y_data[frame]

    #laser_rotate[0] = dx* numpy.cos(angle) - dy * numpy.sin(angle) + x_data[frame]
    #laser_rotate[1] = dx * numpy.sin(angle) + dy * numpy.cos(angle) + y_data[frame]
   

#graph config 
def set_ax():
    ax.set_xlim(0,8)
    ax.set_ylim(0,8)
    ax.grid()

def update(frame):
    if frame > 1:
        x_line.pop(0)
        y_line.pop(0)
    

    x_line.append(x_data[frame])
    y_line.append(y_data[frame])
    if len(x_line) > 3:
        x_line.pop(0)
        y_line.pop(0)

    #print(x_line,"frame:",frame)
    #print(y_line,"frame:",frame)

    #laser_x[0][0] = x_data[frame]
    #laser_x[0][1] = x_data[frame]

    #laser_y[0][0] = y_data[frame]
    #laser_y[0][1] = y_data[frame]+5
    for i in range(10):   
        laser_x[i] = [4  + rcl[i],4]
        laser_y[i] = [4,6]


    rotate_laser(cangle[frame],frame)


    ax.cla()
    set_ax()
    #ax.plot(x_data[frame],y_data[frame],marker=(3,0,180 + cangle[frame]),markersize=50)
    ax.plot(4,4,marker=(3,0,180 + cangle[frame]),markersize=50)
    ax.plot(x_line,y_line)
    for i in range(10):
        plotlaser_x = [laser_x[i][0],laser_rotate[i][0]]
        plotlaser_y = [laser_y[i][0],laser_rotate[i][1]]

        ax.plot(plotlaser_x,plotlaser_y)


    if frame == 9:
        for i in range(10):
            x_data[i] = random.randint(0,8)
            y_data[i] = random.randint(0,8)
            set_label()


def destroy_window():
    root.quit()
    root.destroy()


root = tk.Tk()

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.set_aspect('equal',adjustable='box')


#range of center to laser
rcl = [-0.5,-0.4,-0.3,-0.2,-0.1,0.1,0.2,0.3,0.4,0.5]
#[laser current x position,  laser end x position]
laser_x= [[0]*2 for i in range(10)] 
#[laser current  y position,  laser end y position]
laser_y= [[0]*2 for i in range(10)] 
#laser length
laser_length = [] * 10

laser_rotate = [[0] * 2 for i in range(10)]

laser_replace = [[0] * 2 for i in range(10)]

cangle = [0,30,60,90,120,150.180,210,240,270,300]

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side='left')

label1 = tk.Label(root,width=15,bg="#fff")
label2 = tk.Label(root,width=15,bg="#fff")
label3 = tk.Label(root,width=15,bg="#fff")
label4 = tk.Label(root,width=15,bg="#fff")
label5 = tk.Label(root,width=15,bg="#fff")
label6 = tk.Label(root,width=15,bg="#fff")
label7 = tk.Label(root,width=15,bg="#fff")
label8 = tk.Label(root,width=15,bg="#fff")
label9 = tk.Label(root,width=15,bg="#fff")
label10 = tk.Label(root,width=15,bg="#fff")

label1.pack(side='top')
label2.pack(side='top')
label3.pack(side='top')
label4.pack(side='top')
label5.pack(side='top')
label6.pack(side='top')
label7.pack(side='top')
label8.pack(side='top')
label9.pack(side='top')
label10.pack(side='top')

set_label()



ani = FuncAnimation(fig,update,frames=10,interval=2000)

button = tk.Button(master=root,
                   text="NIT SUZUKA",
                   command=destroy_window,
                   bg="#fff",
                   width=10,height=3,
                   )
button.pack()


tk.mainloop()