import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "./day-25/US-State-Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
data = pd.read_csv('./day-26/US-State-Game/50_states.csv')
all_states =  data.state.to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name? ").title()
    
    if answer_state == 'Exit':
        states_not_in_guessed = []
        for state in all_states:
            if state not in guessed_states:
                states_not_in_guessed.append(state)

        dict_learn_state = {
            'State': states_not_in_guessed
        }

        df = pd.DataFrame(dict_learn_state)
        df.to_csv('./day-25/US-State-Game/states_to_learn.csv')
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        s = turtle.Turtle()
        s.hideturtle()
        s.penup()
        state_data = data[data.state == answer_state]
        s.goto(state_data.x.item(), state_data.y.item())
        s.write(state_data.state.item())


