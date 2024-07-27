import tkinter as tk
from tkinter import messagebox

class Pop_up:
    def __init__(self):
        self.window = tk.Tk()
        self.window.withdraw()  # Initially hide the main window

    def open_pop_up(self, title, message):
        self.score = None  # Initialize score as None
        pop_up_window = tk.Toplevel(self.window)  # Create a new window on top of the main window
        pop_up_window.title(title)
        
        tk.Label(pop_up_window, text=message).pack()  # Display the message
        
        entry_field = tk.Entry(pop_up_window)
        entry_field.pack()
        
        def on_submit():
            score = int(entry_field.get())
            if score != 0:  # If score is non-zero, it means a valid integer was entered
                self.score = score
                pop_up_window.destroy()  # Close the pop-up window
            else:
                messagebox.showerror("Error", "Please enter a valid integer")
        
        submit_button = tk.Button(pop_up_window, text="Submit", command=on_submit)
        submit_button.pack()
        
        self.window.wait_window(pop_up_window)  # Wait for the pop-up window to close
        return self.score  # Return the score after the pop-up window is closed

    def notify_pop_up(self, title, message):
        messagebox.showinfo(title=title, message=message)
