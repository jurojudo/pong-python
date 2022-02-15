import turtle
import winsound

window = turtle.Screen()
window.title("Pong by Juro")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.penup()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.penup()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.shape("square")
ball.color("white")
ball.goto(0, 0)
ball.dx = 0.08
ball.dy = 0.08

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.color("white")
pen.goto(0, 250)
pen.write("Player A: 0  Player B: 0", align="center",  font=("Courier", 18, "normal"))

# Function


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    if paddle_a.ycor() > 360:
        paddle_a.sety(-340)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    if paddle_a.ycor() < -360:
        paddle_a.sety(340)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    if paddle_b.ycor() > 360:
        paddle_b.sety(-340)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    if paddle_b.ycor() < -360:
        paddle_b.sety(340)

# Keyboard bindings


window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # Ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce (1).wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce (1).wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

    # Ball and paddle collision
    if 350 > ball.xcor() > 340 and paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce (1).wav", winsound.SND_ASYNC)

    if -340 > ball.xcor() > -350 and paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce (1).wav", winsound.SND_ASYNC)
