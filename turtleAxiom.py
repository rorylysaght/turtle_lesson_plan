import turtle
import random

tom = turtle.Turtle()
tom.speed(10)
colors  = ["red","green","blue","orange","purple","olive","yellow", "cyan", "magenta", "lime"]

for i in range(12):
  tom.color(random.choice(colors))
  for i in range(2):
    tom.forward(100)
    tom.right(60)
    tom.forward(100)
    tom.right(120)
  tom.right(30)

#required on mac/pc to keep window open after drawing
turtle.done()
