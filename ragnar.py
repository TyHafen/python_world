import turtle


# step 2
player_dx = 15


def move_left():
    x = player.xcor()-player_dx
    # if statement sets limit on how far wee can move left
    if x < -190:
        x = -190
    player.setx(x)


def move_right():
    x = player.xcor()+player_dx
    # if statement sets limit on how far wee can move right
    if x > 190:
        x = 190
    player.setx(x)

# End step 2

# Start step 5


def fire_bullet():
    x = player.xcor()
    y = player.ycor()
    bullet.setposition(x, y+30)
    bullet.showturtle()


# This is step 1
# Set up window
wn = turtle.Screen()
wn.setup(width=540, height=540)
wn.bgcolor("black")
wn.title("Space Invaders")
# Draw a border
border = turtle.Turtle()
border.speed(0)
border.color("green")
border.up()
border.setposition(-200, -200)
border.down()
border.pensize(3)

for side in range(4):
    border.forward(400)
    border.left(90)
border.hideturtle()

# register shape
turtle.register_shape("images/rocket.gif")
turtle.register_shape("images/alien.gif")


# Create player
player = turtle.Turtle()
player.shape("images/rocket.gif")
player.up()
player.speed(0)
player.setposition(0, -180)

invader = turtle.Turtle()
invader.shape("images/alien.gif")
invader.up()
invader.speed(0)
invader.setposition(-180, 180)

# End step 1

# step 4
# create players bullet
bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("triangle")
bullet.up()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5, .5)
bullet.hideturtle()

# end step 4


# step 3
# create keyboard binding
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

invader_speed = 2
bullet_speed = 10

while True:
    invader.forward(invader_speed)
    if invader.xcor() > 190 or invader.xcor() < -190:
        invader.right(180)
        invader.forward(invader_speed)

    bullet.forward(bullet_speed)


turtle.mainloop()
