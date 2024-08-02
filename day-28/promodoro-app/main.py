from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
ticks = ''

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_title.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text= '00:00') 
    global reps, ticks
    reps = 0
    ticks = ''
    tick_label.config(text=ticks)
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_sec = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    if reps %8 == 0:
        count_down(long_break_seconds)
        timer_title.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        timer_title.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        timer_title.config(text='Work', fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min =  math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f'0{round(count_seconds)}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps, ticks
        for _ in range(math.floor(reps/2)):
            ticks += '✔'
        tick_label.config(text=ticks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Promodoro')
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width= 200, height=224, bg= YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='./day-28/promodoro-app/tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text= '00:00', fill='white', font=(FONT_NAME, 29, 'bold'))
canvas.grid(column=2, row=2)

timer_title = Label(text='Timer', fg= GREEN, font=(FONT_NAME, 35), bg=YELLOW, highlightthickness=0)
timer_title.grid(column=2, row=1)

start_btn = Button(text='Start', highlightthickness=0, command= start_timer)
start_btn.grid(column=1, row=3)
reset_btn = Button(text='Reset', highlightthickness=0, command= reset_timer)
reset_btn.grid(column=3, row=3)

tick_label = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 20, 'bold'))
tick_label.grid(column=2, row=4)


window.mainloop()