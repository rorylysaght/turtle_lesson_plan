import turtle
import random

pat = turtle.Turtle()
pat.speed(500)
colors = ['red', 'green', 'blue', 'purple', 'orange', 'pink']

for x in range(1, 10, 2):
    for i in range(6):
        for i in range(2):
            pat.forward(x*10)
            pat.right(60)
            pat.forward(x*10)
            pat.right(120)
        pat.right(60)
        pat.color(random.choice(colors))

turtle.done()
