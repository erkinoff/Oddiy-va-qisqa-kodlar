import turtle
colors = ['red','purple','blue','green','orange','yellow']
t = turtle.Pen()
turtle.bgcolor("black")

for x in range(9999):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(60)
    t.speed(9999999999999999)
