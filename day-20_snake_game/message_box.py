import tkinter as tk
from tkinter import messagebox

class Pop_up:
    def __init__(self) :
        self.window = tk.Tk()
        
    def open_pop_up(self, title, message):
        self.window.withdraw()
        messagebox.showinfo(title=title, message=message)