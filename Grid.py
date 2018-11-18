from graphics import *
from time import time
class box:
    def __init__(self, tileSize, x, y):
        self.depth = 2
        self.tileSize = tileSize
        self.x = x
        self.y = y
        self.centreX = self.tileSize//2*x
        self.centreY = self.tileSize//2*y

    def Draw(self, win):
        coord1x = self.centreX-(self.tileSize//2)+self.depth
        print(self.centreX)
        print(self.centreY)
        print(coord1x)
        coord1y = self.centreY-(self.tileSize//2)+self.depth
        print(coord1y)
        
        coord2x = self.centreX+(self.tileSize//2)-self.depth
        print(coord2x)
        coord2y = self.centreY+(self.tileSize//2)-self.depth
        print(coord2y)
        point1 = Point(coord1x, coord1y)
        point2 = Point(coord2x, coord2y)
        r = Rectangle(point1, point2)
        r.setFill("white")
        r.draw(win)

    

def main():
    tiles, win = init(500, 500, 2)
    display(tiles, win)
    update(30)
    win.getMouse()
    win.close()

def init(x, y, num):
    win = GraphWin("Grid", x, y, autoflush=False)
    win.setBackground("black")
    numX = 0
    numY = 0
    tileSize = 0
    if x < y:
        tileSize = y // num 
        numY = num
        numX = x // tileSize

    elif x > y:
        tileSize = x // num 
        numX = num
        numY = y // tileSize

    else:
        tileSize = x // num
        numX = num
        numY = num

    tiles = [0] * numX
    for i in range(numX):
        tiles[i] = [0] * numY

    for i in range(numX):
        for j in range(numY):
            tiles[i][j] = box(tileSize, i, j)
    
    return tiles, win


def display(tiles, win):
    for i in range(len(tiles)):
        for j in range(len(tiles[i])):
            tiles[i][j].Draw(win)

main()