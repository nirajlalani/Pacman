import math
import os


def floor(value,size,offset=200):

    return float(((value+offset) // size) * size - offset)




def line(a,b,x,y):

    """
    Draw a line from (a,b) to (x,y)
    """

    import turtle
    turtle.up()
    turtle.goto(a,b)
    turtle.down()
    turtle.goto(x,y)


def square(x,y,sideLength,colourFill):

    """
    Drawing square at '(x,y)' with length of the side as 'sideLength'
    and colour filling as 'colourFill'.
    
    This square will have '(x,y)' at its left bottom corner.
    """

    import turtle
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color(colourFill)
    turtle.begin_fill()
    turtle.speed(1)

    for _ in range(4):
        turtle.fd(sideLength)
        turtle.lt(90)

    turtle.end_fill()


class vector():

    """
    Two dimensional vector
    """

    precision = 5

    __slots__ = ("_x","_y","_hash")


    def __init__(self,x,y):

        """
        Initialize vector with (x,y)
        """

        self._hash = None
        self._x = round(x,self.precision)
        self._y = round(y,self.precision)


    @property
    def x(self):

        """
        X-axis component of the vector
        """

        return self._x


    @x.setter
    def x(self,xValue):
        if self._hash != None:
            raise ValueError("Cannot set x after hashing")
        self._x = round(xValue,self.precision)

    @property
    def y(self):
        """
        Y-axis component of the vector
        """

        return self._y

    @y.setter
    def y(self, yValue):
        if self._hash != None:
            raise ValueError("Cannot set y after hashing")
        self._y = round(yValue, self.precision)


    def __hash__(self):

        """
        Hashing the vector
        """

        if self._hash == None:
            pair = (self.x,self.y)
            self._hash = hash(pair)
        else:
            print("Cannot set hash")
        return self._hash


    def __len__(self):

        """
        Length of the vector
        """

        return 2


    def __getitem__(self, index):

        if index == 1:
            return self.x
        elif index == 2:
            return self.y
        else:
            raise IndexError


    def copy(self):

        """
        Make copy of a vector
        """

        copy_self = type(self)
        return copy_self(self.x,self.y)

    def __eq__(self, other):

        """
        checking two vectors are equal or not
        """

        if isinstance(other, vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented


    def __ne__(self, other):

        """
        checking two vectors are not equal or not
        """

        if isinstance(other, vector):
            return self.x != other.x or self.y != other.y
        return NotImplemented


    def move(self,other):

        """
        adding the parameters of two vectors
        """

        if self._hash != None:
            raise ValueError
        else:
            self.x += other.x
            self.y += other.y
        return self


    def rotate(self,angle):
        if self._hash != None:
            raise ValueError
        else:
            radian = angle * math.pi / 180
            cosine = math.cos(radian)
            sine = math.sin(radian)
            x = self.x
            y = self.y
            self.x = x * cosine - y * sine
            self.y = y * cosine - x * sine
