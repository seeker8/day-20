from turtle import Turtle, Screen
import time

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    segment = Turtle("square")
    segment.penup()
    segment.color("white")
    segment.goto(position)
    segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment_num in range(len(segments)-1, 0, -1):
        segments[segment_num].goto(segments[segment_num-1].xcor(), segments[segment_num-1].ycor())
    segments[0].forward(20)
    segments[0].left(90)



screen.exitonclick()