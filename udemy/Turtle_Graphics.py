from turtle import Turtle, Screen
import random

Turtle_G = Turtle()
Turtle_G.shape("turtle")
Turtle_G.color("Black")


Turtle_G.hideturtle()
Turtle_G.pensize(10)
Turtle_G.speed(10)

move_distance = 25
for _ in range(300):
    # 랜덤하게 이동 방향 선택
    direction = random.choice(['north', 'south', 'east', 'west'])
    color = (random.random(), random.random(), random.random())

    Turtle_G.color(color)
    # 선택된 방향으로 거북이 이동
    if direction == 'north':
        Turtle_G.setheading(90)  # 북쪽으로 향하도록 설정
        Turtle_G.forward(move_distance)
    elif direction == 'south':
        Turtle_G.setheading(270)  # 남쪽으로 향하도록 설정
        Turtle_G.forward(move_distance)
    elif direction == 'east':
        Turtle_G.setheading(0)  # 동쪽으로 향하도록 설정
        Turtle_G.forward(move_distance)
    elif direction == 'west':
        Turtle_G.setheading(180)  # 서쪽으로 향하도록 설정
        Turtle_G.forward(move_distance)

screen = Screen()
screen.exitonclick()