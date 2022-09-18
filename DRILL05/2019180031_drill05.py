import turtle

def ResetGame():                #리셋
    turtle.reset()

def GoForward():                #앞(W)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def GoBack():                   #뒤(S)
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def GoLeft():                   #왼쪽(A)
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def GoRight():                  #오른쪽(D)
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()


turtle.shape('turtle')

turtle.onkey(GoForward,"w")
turtle.onkey(GoBack,"s")
turtle.onkey(GoLeft,"a")
turtle.onkey(GoRight,"d")
turtle.onkey(ResetGame,"Escape")
turtle.listen()
