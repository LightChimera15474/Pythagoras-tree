from random import random, randint
import turtle

# params
rng = 11
axiom = "22222220"
rule = {"0": "1[20]20", "1": '21'}
angle = 20
width = 10
penSize = 16

# colors params
branchColor = "#3d0c02"
leafColors = ["#007046", "#20815D", "#00AC6B", "#00CC00", "#008500", "#7B9E00"]

# window settings
positionX = 0
positionY = turtle.window_height() / -2

# create the programs
for i in range(rng):
    tmpStr = ""
    for key in axiom:
        tmpStr += rule.get(key, key)
    axiom = tmpStr

# turtle settings
turtle.hideturtle()
turtle.penup()
turtle.setposition(positionX, positionY)
turtle.left(90)
turtle.pendown()
turtle.pensize(penSize)
turtle.color(branchColor)
turtle.tracer(50)

stack = []
for command in axiom:
    if command == "1":  # draw branch
        turtle.forward(width)
    elif command == '2':  # draw branch by chance 0.4
        if random() <= 0.4:
            turtle.forward(width)
    elif command == "0":  # draw foliage
        turtle.pensize(penSize * 10)
        color = randint(0, len(leafColors) - 1)  # select the color of leaf
        turtle.color(leafColors[color])
        turtle.forward(width - 5)
        turtle.color(branchColor)  # change the color back to branch color
    elif command == "[":  # save position and direction to steck
        penSize *= 0.75  # branch thickness reduction
        turtle.pensize(penSize)
        stack.append(penSize)
        stack.append(turtle.xcor())
        stack.append(turtle.ycor())
        stack.append(turtle.heading())
        turtle.left(angle - randint(-8, 8))
    elif command == "]":  # load position and direction from steck
        turtle.penup()
        turtle.setheading(stack.pop())
        turtle.sety(stack.pop())
        turtle.setx(stack.pop())
        penSize = stack.pop()
        turtle.pensize(penSize)
        turtle.pendown()
        turtle.right(angle - randint(-8, 8))

turtle.update()
turtle.done()
