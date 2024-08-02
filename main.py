from turtle import Turtle, Screen
import random

screen = Screen()


def setting_screen():
    screen.setup(width=500, height=400)  # setting the size of screen
    screen.bgcolor("LightYellow")
    tim = Turtle()
    tim.penup()
    tim.hideturtle()
    tim.speed(0)
    tim.goto(0, 180)
    tim.pencolor("LightSlateGray")
    tim.write("Turtle Race", align="center", font=("courier", 15, "bold"))
    tim.pencolor("black")
    tim.goto(-210, 100)
    tim.setheading(270)
    tim.pendown()
    tim.forward(200)
    tim.backward(100)
    tim.penup()
    tim.goto(-200, 0)
    tim.write("Start", True, font=("courier", 12, "bold"))

    tim.setheading(0)
    tim.forward(380)
    tim.pendown()
    tim.setheading(90)

    tim.forward(110)
    tim.setheading(270)
    tim.forward(220)
    tim.penup()
    tim.goto(180, 0)

    tim.write("Finish", True, font=("courier", 10, "bold"))


setting_screen()

user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a colour:")
colors = ["red", "yellow", "green", "purple", "orange", "blue"]
is_race_on = False
y_cor = -70
turtles_list = []

if user_bet:
    is_race_on = True

    for i in range(6):
        new_turtle = Turtle(shape="turtle")
        tom_color = random.choice(colors)

        turtles_list.append(new_turtle)
        new_turtle.color(tom_color)
        colors.remove(tom_color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_cor)
        y_cor += 30

    winner_turtle = " "
    while is_race_on:
        for turtle in turtles_list:
            steps = random.randint(0, 10)
            turtle.forward(steps)  # to move the turtle by random steps
            if round(turtle.xcor(), 0) > 230:  # to check if any turtle has crossed the finish line
                winner_turtle = turtle.pencolor()  # to get color of the winner turtle
                is_race_on = False

        if not is_race_on:
            break

    if user_bet == winner_turtle:
        print(f"You've won! The winner is {winner_turtle}")
    else:
        print(f"You've lost! The winner is {winner_turtle}")


else:
    print("Please make your bet!")

screen.exitonclick()
