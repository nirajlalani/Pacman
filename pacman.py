from random import *
from turtle import *
from base import *

path = Turtle()

aim = vector(10,0)
pacman = vector(-20,-120)

ghosts = [
          [vector(-200,180),vector(5,0)],
          [vector(-200,-180),vector(0,5)],
          [vector(180,180),vector(0,-5)],
          [vector(180,-200),vector(-5,0)]
         ]

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


def offset(point):
    x = (floor(point.x,20)+200)/20
    y = (180-floor(point.y,20))/20
    index = int(x+y*20)
    return index

def valid(point):
    
    index = offset(point)
    if tiles[index] == 0:
        return False

    index = offset(point+19)
    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def move():

    clear()
    
    if valid(pacman + aim):
        ht()
        pacman.move(aim)
        
    index = offset(pacman)
    if tiles[index] == 1:
        tiles[index] = 2
        x = (index%20)*20 - 200
        y = 180 - (index//20)*20
        ht()
        square(x,y)

    up()
    goto(pacman.x +10 , pacman.y +10)
    dot(20,'yellow')

    for point,course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [vector(5,0),
                       vector(-5,0),
                       vector(0,5),
                       vector(0,-5)]

            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x+10 , point.y+10)
        dot(20,'red')
    update()

    for point,course in ghosts:
        if abs(pacman - point)<20:
            return

    ontimer(move,100)



def world():
    bgcolor("black")
    path.color("blue")

    for i in range(len(tiles)):
        if tiles[i] > 0:
            x = (i%20)*20 -200
            y = 180 - (i//20)*20
            square(x,y)

            if tiles[i]==1:
                
                path.up()
                path.goto(x+10,y+10)
                path.dot(2,"white")

def change(x,y):
    temp = vector(x,y)
    if valid(pacman+temp):
        aim.x = x
        aim.y = y


setup(420,420,500,150)
ht()
tracer(False)
listen()

onkey(lambda: change(10,0),"Right")
onkey(lambda: change(10,0),"Left")
onkey(lambda: change(10,0),"Up")
onkey(lambda: change(10,0),"Down")


world()
move()
done()



