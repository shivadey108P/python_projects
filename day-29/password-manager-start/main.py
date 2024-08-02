from tkinter import *
from tkinter import messagebox
from password_generator import GeneratePassword
import pyperclip

PADX = 5
PADY = 5

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
generator = GeneratePassword()

def password_generator():
    password_field.delete(0, END)
    new_password = generator.generate_password()
    password_field.insert(0, string=new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email_or_username_text = email_username_field.get()
    password_text = password_field.get()
    website_text = website_field.get()
    
    if len(website_text) == 0 or len(email_or_username_text) == 0 or len(password_text) == 0:
        messagebox.showerror(title= 'Oops', message="Please don't leave any fields empty")
    else:
        is_ok =  messagebox.askokcancel(title=website_text, message=f"These are the details entered: \n     Email/Username: {email_or_username_text}\n     Password:{password_text}")
        
        if is_ok:
            with open('./day-29/password-manager-start/data.txt',mode='a') as file:
                file.write(f"{website_text} | {email_or_username_text} | {password_text}\n")
            password_field.delete(0, END)
            website_field.delete(0, END)
            website_field.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file='./day-29/password-manager-start/logo.png')
canvas.create_image(100,100, image=lock_image)
canvas.grid(row=1, column=2)

website_label = Label(text='Website:')
website_label.grid(row=2, column=1, padx=PADX, pady=PADY)

website_field = Entry(width=47)
website_field.grid(row=2, column=2, columnspan=2, padx=PADX, pady=PADY)
website_field.focus()

email_username_label = Label(text='Email/Username:')
email_username_label.grid(row=3, column=1, padx=PADX, pady=PADY)

email_username_field = Entry(width=47)
email_username_field.grid(row=3, column=2, columnspan=2, padx=PADX, pady=PADY)
email_username_field.insert(0, 'shivadey1089@gmail.com')

password_label = Label(text='Password:')
password_label.grid(row=4, column=1, padx=PADX, pady=PADY)

password_field = Entry(width=27)
password_field.grid(row=4, column=2, padx=PADX, pady=PADY)

generate_password_btn = Button(text='Generate Password', command=password_generator)
generate_password_btn.grid(row=4, column=3, padx=PADX, pady=PADY)

add_btn = Button(text='Add', width=46, command=save)
add_btn.grid(row=5, column=2, columnspan=2, padx=PADX, pady=PADY)

window.mainloop()