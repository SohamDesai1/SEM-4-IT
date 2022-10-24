import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
n = 500
h = 0
for i in range(240):
    c = colorsys.hsv_to_rgb(h, 1.0, 0.8)
    h += 1 / n
    t.color(c)
    for j in range(2):
        t.left(250)
        t.forward(i * 3)
        t.left(2)
        t.forward(2)
