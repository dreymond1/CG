import turtle
import math

screen = turtle.Screen()

for i in range(1300):
    vt = i/40*math.pi
    y = (vt*5+5)*math.sin(vt)
    x = (vt*5+5)*math.cos(vt)
    turtle.goto(x, y)
screen.exitonclick()
