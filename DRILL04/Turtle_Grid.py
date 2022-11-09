import turtle

turtle.penup()
t_x = -300
t_y= 300
turtle.goto(t_x,t_y)
turtle.pendown()
turtle.setheading(0)

for i in range(6):
    turtle.forward(500)
    turtle.penup()
    t_y -= 100
    turtle.goto(t_x,t_y)
    turtle.pendown()
    
turtle.penup()
t_x=-300
t_y=300
turtle.goto(t_x,t_y)
turtle.setheading(270)
turtle.pendown()

for i in range(6):
    turtle.forward(500)
    turtle.penup()
    t_x += 100
    turtle.goto(t_x,t_y)
    turtle.pendown()

turtle.exitonclick()
