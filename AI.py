import random as r
import matplotlib.pyplot as plt
import time as t

desired = [5,5]
n = 10
gen = list()
scores = list()
tries = 10
bx = 0
by = 0
xmod = 0
ymod = 0
berror = 0
lbx = 0
lby = 0
#ran = range of "target board"
ran = 10

for i in range(tries):
    genx = list()
    geny = list()

    for i in range(n):
        dx = ((r.random()-0.5)*(berror/10)+(xmod*(berror/ran))+bx)
        dy = ((r.random()-0.5)*(berror/10)+(ymod*(berror/ran))+by)
        genx.append(dx)
        geny.append(dy)

    

    for i in range(len(genx)):
        gen.append([genx[i],geny[i]])

    for i in gen:
        xerror = (desired[0]-i[0])**2
        yerror = (desired[1]-i[1])**2
        error = xerror + yerror
        scores.append([error,i])

    scores.sort()

    berror = scores[0][0]

    print()
    print(scores[0])
    print()
    bx = scores[0][1][0] - xmod
    by = scores[0][1][1] - ymod
    xmod = scores[0][1][0]
    ymod = scores[0][1][1]
    print(berror)
    print(xmod,ymod)
    print(bx,by)

    plotx = list(genx)
    ploty = list(geny)
    plt.scatter(0,0,color="k")
    plt.scatter(10,10,color="k")
    plt.scatter(genx,geny)
    plt.scatter(scores[0][1][0],scores[0][1][1],color="r")
    plt.scatter(desired[0],desired[1],color="y")
    plt.scatter(lbx,lby,color="g")
    plt.show()


    t.sleep(1)
    lbx = scores[0][1][0]
    lby = scores[0][1][1]
    