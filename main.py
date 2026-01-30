from turtle import Turtle, Screen

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
jiji = Turtle(shape="square")
jiji.color("white")
jiji.penup()

stamp_id = 0
def draw_snake(length):
    for i in range(length):
        jiji.stamp()
        jiji.forward(20)

for _ in range(10):
    jiji.clearstamps()
    draw_snake(3)



screen.exitonclick()