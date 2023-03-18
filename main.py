import turtle
import pandas
from turtle import Turtle
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim = Turtle()
tim.hideturtle()
num = 0
state_list = []
game_is_on = True
while game_is_on:
    answer_state = turtle.textinput(title=f"({num}/50) states correct",
                                    prompt="What's the another state's name?").capitalize()
    if answer_state == "Exit":
        break
    states = pandas.read_csv("50_states.csv")
    state = states["state"]
    for single_state in state:
        if answer_state == single_state:
            state_list.append(answer_state)
            n = states[states.state == single_state]
            x = int(n.x)
            y = int(n.y)
            tim.penup()
            tim.goto(x, y)
            tim.write(single_state)
            num += 1
        elif num >= 50:
            game_is_on = False
final_list = []
for x in state:
    if x not in state_list:
        final_list.append(x)
data = pandas.DataFrame(final_list)
data.to_csv("new_csv")
# turtle.mainloop()
