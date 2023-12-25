import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = screen.textinput(
    title="Guess the State", prompt="What's another state's name?"
)

data = pandas.read_csv("50_states.csv")


row = data[data.state == answer_state.capitalize()]

if row.empty:
    print("Not in list")
else:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(row.x.item(), row.y.item())
    t.write(row.state.item())

screen.exitonclick()
