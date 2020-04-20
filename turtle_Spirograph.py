import turtle, random

colors = ['red', 'green', 'blue', 'purple', 'cyan', 'magenta', 'orange']

tom = turtle.Turtle()
tom.color('purple')
tom.speed(100)

#triangle
for x in range(36):
  tom.color(random.choice(colors))
  tom.forward(200)
  tom.right(120)
  tom.forward(200)
  tom.right(120)
  tom.forward(200)
  tom.right(10)

for x in range(6):
  tom.color(random.choice(colors))
  for x in range(2):
    tom.forward(110)
    tom.right(60)
    tom.forward(110)
    tom.right(120)
  tom.right(60)

for x in range(12):
  tom.color(random.choice(colors))
  for x in range(2):
    tom.forward(105)
    tom.right(60)
    tom.forward(105)
    tom.right(120)
  tom.right(30)


for x in range(120):
  tom.color(random.choice(colors))
  for x in range(2):
    tom.forward(100)
    tom.right(60)
    tom.forward(100)
    tom.right(120)
  tom.right(3)

turtle.done()
