'''To read data from file and plot'''
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('Solarize_Light2')
fig=plt.figure()
ax=fig.add_subplot(2,2,1)

def animate(i):
    graphdata=open('data.txt','r').read()
    lines=graphdata.split('\n')
    xs=[]
    ys=[]
    for line in lines:
            '''if len(line)>1:'''
            x,y=line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax.clear()
    ax.plot(xs,ys)
    ax.set_xlabel('Mission time')
    ax.set_title('Plot 1')

ani=animation.FuncAnimation(fig,animate,interval=1000)


bx=fig.add_subplot(2,2,2)

def animate2(i):
    graphdata2=open('data2.txt','r').read()
    lines2=graphdata2.split('\n')
    xs2=[]
    ys2=[]
    for line2 in lines2:
        x2,y2=line2.split(',')
        xs2.append(float(x2))
        ys2.append(float(y2))
    bx.clear()
    bx.plot(xs2,ys2)
    bx.set_xlabel('Mission time')
    bx.set_title('Plot 2')


ani2=animation.FuncAnimation(fig,animate2,interval=1000)

cx=fig.add_subplot(2,2,3)
def animate3(i):
    graphdata3=open('data3.txt','r').read()
    lines3=graphdata3.split('\n')
    xs3=[]
    ys3=[]
    for line3 in lines3:
        x3,y3=line3.split(',')
        xs3.append(float(x3))
        ys3.append(float(y3))
    cx.clear()
    cx.plot(xs3,ys3)
    cx.set_xlabel('Mission time')
    cx.set_title('Plot 3')


ani3=animation.FuncAnimation(fig,animate3,interval=1000)

dx=fig.add_subplot(2,2,4)
def animate4(i):
    graphdata4=open('data4.txt','r').read()
    lines4=graphdata4.split('\n')
    xs4=[]
    ys4=[]
    for line4 in lines4:
        x4,y4=line4.split(',')
        xs4.append(float(x4))
        ys4.append(float(y4))
    dx.clear()
    dx.plot(xs4,ys4)
    dx.set_xlabel('Mission time')
    dx.set_title('Plot 4')


ani4=animation.FuncAnimation(fig,animate4,interval=1000)
fig.tight_layout()
plt.subplots_adjust(hspace=0.3)
plt.show()

