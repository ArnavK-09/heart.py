# imports
import turtle as TT

# setup window
def setupWindow():
    # new window
    window = TT.Screen()

    # window config
    window.screensize(300, 300)
    window.title("Heart In Python!")
    window.bgcolor("#f7c1c1")

    # return
    return window

# create turtle 
def createTurtle():
    # init turtle
    t = TT.Turtle()
    
    # turtle config
    t.speed(3)
    t.pencolor("#e31305")
    t.width(2)
    t.shape("classic")

    # return
    return t

# curve functon
def curve(t):
    for i in range(200):
        t.right(1)
        t.forward(1)
        
# create space for text
def createSpaceForText(t):
    t.home()
    t.penup()
    t.right(90)
    t.forward(30)

# heart func
def createHeart(t):
    # start
    t.fillcolor("#e31305")
    t.begin_fill()
    t.left(140)
    t.forward(115)

    # curves
    curve(t)
    t.left(121)
    curve(t)
    t.forward(113)

    # end 
    t.end_fill()

# main start
def main(message: str = "Heart Done!"):
    # log
    print("Started Creating Heart!")
    
    # setup window
    screen = setupWindow()
    
    # turtle
    turtle = createTurtle()

    # prevent resize
    try:
        screen.cv._rootwindow.resizable(False, False)
    except:
        pass
    
    # create heart
    createHeart(turtle)

    # hide turtle
    turtle.hideturtle()

    # create space for text
    createSpaceForText(turtle)

    # message write 
    turtle.write(message, True, align="center", font=('Comic Sans MS', 15, 'normal'))

    # log
    print("Created Heart!")

    # for exit
    screen.exitonclick()
