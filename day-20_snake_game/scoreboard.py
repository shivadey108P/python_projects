from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Removed self from super().__init__(self)
        self.color('white')
        self.score = 0
        self.high_score = self.get_high_score()
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.speed('fastest')   
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}   High Score: {self.high_score}', align=ALIGNMENT, font=FONT)
        
    def reset_game(self):
        self.clear()
        self.update_high_score()
        self.score = 0
        self.update_scoreboard()
        
    def get_high_score(self):
        with open('python_projects\\day-20_snake_game\\data.txt', mode= 'r') as file:
            return int(file.read())
            
    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('python_projects\\day-20_snake_game\\data.txt', mode= 'w') as file:
                file.write(str(self.high_score))
                
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('Game Over', align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()