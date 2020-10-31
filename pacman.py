from random import *
from turtle import *

from GameBase import *

path = Turtle()
#pacman = vector()
#aim = vector()
#ghosts = [vector()]

tiles = [

1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,
1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,
1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,
1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,
0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,
0,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,
1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,
1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,1,
0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,
0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,
1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,1,
1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,
0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,0,
0,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,1,0,
1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,
1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,
1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,
1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,
1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,
        ]


def square(x, y):
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def world():
    bgcolor("black")
    path.color("blue")

    for i in range(len(tiles)):
        tile = tiles[i]
        if tile > 0:
            x = (i%20)*20 -200
            y = 180 - (i//20)*20
            square(x,y)
            path.up()
            path.goto(x+10,y+10)
            path.dot(2,"white")



setup(420,420,370,0)
ht()
tracer(False)
world()
done()



