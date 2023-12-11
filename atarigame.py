import turtle


# Pantalla
wn = turtle.Screen()
wn.title("Atari Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Cargar formas
wn.addshape("boton.gif")
wn.addshape("boton1.gif")
wn.addshape("pong.gif")
wn.addshape("jugador1.gif")
wn.addshape("jugador2.gif")

# Atari logo
logo = turtle.Turtle()
logo.shape("pong.gif")
logo.penup()
logo.goto(0, 150)

# Botón
start = turtle.Turtle()
start.shape("boton.gif")
start.penup()
start.goto(0, 0)

# jugador 1 
jugador1 = turtle.Turtle()
jugador1.shape("jugador1.gif")
jugador1.penup()
jugador1.goto(0,0)
jugador1.shapesize(stretch_wid=2, stretch_len=6)
jugador1.hideturtle()

#jugador 2 
jugador2 = turtle.Turtle()
jugador2.shape("jugador2.gif")
jugador2.penup()
jugador2.goto(0, -75)
jugador2.hideturtle()

    
def on_button_press():
    start.shape("boton1.gif")

def on_button_release():
    start.shape("boton.gif")
    start.hideturtle()
    logo.hideturtle()
    jugador1.showturtle()
    jugador2.showturtle()
#def on_click(x, y):
    #print(f"Clicked at position ({x}, {y})")

def on_click(x, y):
    if on_button_release:
     if -109 <= x <= 102 and -10 <= y <= 25:
         print("game for 1")  
     elif -110<= x <=104 and -95 <= y <= -57:
         print("game for 2")

turtle.listen()
turtle.onkeypress(on_button_press, "space")
turtle.onkeyrelease(on_button_release, "space")
turtle.onscreenclick(on_click)


#loope
def close_window():
    try:
        wn.bye()
    except turtle.Terminator:
        pass

wn.onkeypress(close_window, "Escape")
wn.listen()

# loop
while True:
    try:
        wn.update()
    except turtle.Terminator:
        break