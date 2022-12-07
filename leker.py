import time as t

y1,y2,y3,y4,y5,y6,y7,y8,y9,y10 = list(),list(),list(),list(),list(),list(),list(),list(),list(),list()

grid = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]

for i in range(len(grid)):
    for n in range(10):
        grid[i].append(" ")

print(len(grid), len(grid[0]),grid[0][0])

def prnt():
    print("+-+-+-+-+-+-+-+-+-+-+")
    for n in range(len(grid)):
        for i in range(len(grid[n])):
            print("|", grid[n][i], sep="", end="")
        print("|")
        print("+-+-+-+-+-+-+-+-+-+-+")

def clr():
    for i in range(len(grid)):
        for n in range(len(grid[i])):
            grid[i][n]=" "

prnt()

grid[0][0] = "■"

def Tblock(x):
    for i in range(len(grid)):
        grid[i][x-1], grid[i][x], grid[i][x+1], grid[i+1][x] = "■","■","■","■"
        prnt()
        clr()
        t.sleep(0.5)

Tblock(4)