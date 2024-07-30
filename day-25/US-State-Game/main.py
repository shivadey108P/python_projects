import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "./day-25/US-State-Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_cord(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_cord)

usa_states = pd.read_csv('./day-25/US-State-Game/50_states.csv')

count_of_states = len(usa_states.state.values)

game_is_on = True
counter = 0
correct_states = []
while game_is_on:
    answer_state = str(screen.textinput(title=f"{counter}/{count_of_states} States Correct", prompt="What's another state name? ")).lower()

    if answer_state == 'exit':
        game_is_on = False
        break


    if answer_state in usa_states.state.str.lower().values:
        current_state_values = usa_states[usa_states.state.str.lower() == answer_state].to_dict(orient='records')
        state_name = current_state_values[0]['state']
        x = current_state_values[0]['x']
        y = current_state_values[0]['y']
        counter += 1
        correct_states.append(state_name)    
        
        state_name_turtle = turtle.Turtle()
        state_name_turtle.penup()
        state_name_turtle.goto(x=x,y=y)
        state_name_turtle.hideturtle()
        state_name_turtle.write(state_name,align= 'center', font= ('Arial', 10, 'normal'))
    
    else:
        print("State not found")
        
    
# Keep the turtle graphics window open
turtle.mainloop() 