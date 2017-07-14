from turtle import *

sides= int(input("Enter number of sides"))
length= int(input("side length"))
color =  input("color?")
Fast = input("speed?")
fillconferm = input("fill? Y/N")

if fillconferm == "Y" :
    fillconferm(color)
    bengin_fill()
else:
    end_fill()

if not fast:
    speed(6)
else:
    speed(int(fast))

pencolor(color)
angle = 360/sides

for sides in range (int(sides)):
    forward(length)
    right(angle)
    forward(length)
    print ("sides:", sides,"angle:",angle)
end_fill()
exitonclick()
