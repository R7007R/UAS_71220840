import turtle
s = turtle.Screen().bgcolor('pink')
t = turtle.Turtle()


t.pensize(3)



#tongkat coklat
t.down()
t.fillcolor('brown')
t.begin_fill()
t.forward(20)
t.left(90)
t.forward(50)
t.left(90)
t.forward(20)
t.left(90)
t.forward(50)
t.end_fill()
t.up()

#papan kuning

t.goto(0,50)
t.down()
t.fillcolor('yellow')
t.begin_fill()
t.left(90)
t.forward(120)
t.left(45)
t.forward(50)
t.left(45)
t.forward(140)
t.left(45)
t.forward(50)
t.left(45)
t.forward(220)
t.left(45)
t.forward(50)
t.left(45)
t.forward(140)
t.left(45)
t.forward(50)
t.left(45)
t.forward(100)
t.end_fill()
t.up()

#membuat HI!
t.pencolor('red')
t.goto(-25,65)
t.down()
t.left(90)
t.forward(30)
t.backward(15)
t.right(90)
t.forward(30)
t.left(90)
t.forward(15)
t.backward(30)

t.up()
t.goto(15, 65)
t.down()
t.forward(30)

t.up()
t.goto(35, 65)
t.down()
t.forward(1)
t.up()
t.goto(35,75)
t.down()
t.forward(19)
t.up()
t.pencolor('black')

#membuat lingkaran
t.goto(10, 115)
t.down()
t.pencolor('blue')
t.right(90)
t.circle(60, 360)
t.up()

#membuat bintang banyak
t.goto(0,115)
t.down()
t.pencolor('red')

t.right(75)
for i in range(10):
    t.left(108.5)
    t.forward(50)

turtle.done()