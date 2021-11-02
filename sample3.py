import matplotlib.pyplot as plt


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.set_aspect('equal',adjustable='box')
ax.set_xlim(0,8)
ax.set_ylim(0,8)
ax.grid()

xlist = [1,2,3,4,5,6,7,8,9]
ylist = [1,2,3,4,5,6,7,8,9]


for i in range(9):
    plt.plot(i,i,marker='.')
    plt.show()