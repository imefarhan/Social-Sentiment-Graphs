import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

#style.use("ggplot")
style.use("dark_background")
#style.use("presentation")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    pullData = open("twitter-out.txt","r").read()
    lines = pullData.split('\n')

    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines[-200:]:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        xar.append(x)
        yar.append(y)
        
    ax1.clear()
    ax1.plot(xar,yar)
    fig.suptitle('Sentiment Analysis', fontsize=14)
    plt.xlabel('No of Tweets', fontsize=12)
    plt.ylabel('Sentiment Score', fontsize=12)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
