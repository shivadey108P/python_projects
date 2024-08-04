from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ('Ariel', 30, 'italic')
FONT_WORD = ('Ariel', 50, 'bold')

window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx= 50, pady=50)
current_word = {}
try:
    data = pd.read_csv('./day-31/flash-card-project-start/data/words_to_learn.csv')
    words_data = data.to_dict(orient='records')
except FileNotFoundError:
    data = pd.read_csv('./day-31/flash-card-project-start/data/french_words.csv')
    words_data = data.to_dict(orient='records')
except ValueError:
    data = pd.read_csv('./day-31/flash-card-project-start/data/french_words.csv')
    words_data = data.to_dict(orient='records')

    

def is_known():
    global current_word
    words_data.remove(current_word)
    left_to_learn = pd.DataFrame(words_data)
    left_to_learn.to_csv('./day-31/flash-card-project-start/data/words_to_learn.csv', index=False)
    next_word()

def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(words_data)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_word['French'], fill='black')
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)
    
    
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_word['English'], fill='white')
    

card_front = PhotoImage(file='./day-31/flash-card-project-start/images/card_front.png')
card_back = PhotoImage(file='./day-31/flash-card-project-start/images/card_back.png')
canvas =  Canvas(height=526, width= 800, highlightthickness=0, border=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400,263, image= card_front)
card_title = canvas.create_text(400, 150,text='', font=FONT_LANG, fill='black')
card_word = canvas.create_text(400, 300,text='', font=FONT_WORD, fill='black')

flip_timer = window.after(3000, flip_card)

cross_image = PhotoImage(file='./day-31/flash-card-project-start/images/wrong.png')
right_image = PhotoImage(file='./day-31/flash-card-project-start/images/right.png')

cross_btn = Button(image=cross_image, highlightthickness=0, border=0, command= next_word)
right_btn = Button(image=right_image, highlightthickness=0, border=0, command=is_known)

canvas.grid(row=1, column=1, columnspan=2)
cross_btn.grid(row=2, column=1)
right_btn.grid(row=2, column=2)

next_word()

window.mainloop()