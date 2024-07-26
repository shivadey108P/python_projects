score = 10


def get_high_score():
        with open('day-20_snake_game\\snake_game\\day-20_snake_game\\data.txt', mode= 'r') as file:
            return int(file.read())
   
high_score = get_high_score()
         
def update_high_score():
    global high_score
    global score
    if score > high_score:
        high_score = score
        with open('day-20_snake_game\\snake_game\\day-20_snake_game\\data.txt', mode= 'w') as file:
            file.write(str(high_score))
    

update_high_score()        
print(high_score)