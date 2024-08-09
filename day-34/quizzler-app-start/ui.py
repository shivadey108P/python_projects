from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Ariel', 15, 'italic')

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx= 20, pady= 20)
        
        self.score_label = Label(text="Score: 0", font=('Ariel', 12), highlightthickness=0, bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=1, column=2,padx=20, pady=20)
        
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, 
                                                     text='', 
                                                     width= 280,
                                                     fill='black', 
                                                     font=FONT)
        self.canvas.grid(row=2, column=1, columnspan=2,padx=20, pady=20)
        
        self.right_image = PhotoImage(file='./day-34/quizzler-app-start/images/true.png')
        self.wrong_image = PhotoImage(file='./day-34/quizzler-app-start/images/false.png')
        self.right_btn = Button(image=self.right_image, highlightthickness=0, command= self.true_pressed)
        self.right_btn.grid(row=3, column=1, padx=20, pady=20)
        self.wrong_btn = Button(image=self.wrong_image, highlightthickness=0, command= self.false_pressed)
        self.wrong_btn.grid(row=3, column=2,padx=20, pady=20)
        
        self.get_next_question()
                
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached to the end of the quiz")
        
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))
        
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
    