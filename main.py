import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    data = pandas.read_csv("50_states.csv")
    row = data[data.state == answer_state]

    if answer_state == "Exit":
        missing_states = []
        for state in data.state:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break
    if row.empty:
        print("Not in list")
    elif answer_state in guessed_states:
        print("Already guessed")
    else:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(row.x.item(), row.y.item())
        t.write(answer_state)
