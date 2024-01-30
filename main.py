from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make Your Bet!", prompt="Which Turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y = -100
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=y)
    turtles.append(turtle)
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_dist = random.randint(0, 10)
        turtle.fd(rand_dist)


screen.exitonclick()
