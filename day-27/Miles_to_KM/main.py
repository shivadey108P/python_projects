from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=200,height=50)
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_label.config(text=str(round(km,2)))

#Label
miles_label = Label(text= "Miles")
miles_label.grid(column=2, row=0)

#Label
is_equal_to_label = Label(text= "is equal to")
is_equal_to_label.grid(column=0, row=1, padx=5, pady=5)

#Label
km_label = Label(text= "0")
km_label.grid(column=1, row=1, padx=5, pady=5)

#Label
km_text_label = Label(text= "KM")
km_text_label.grid(column=3, row=1, padx=5, pady=5)

def button_click():
    miles_to_km()

#Button
calculate = Button(text='Calculate', command=button_click) 
calculate.grid(column=1, row=2, padx=5, pady=5)


#Entry
miles_input = Entry(width=7)
miles_input.insert(END, '0')
miles_input.grid(column=1, row=0, padx=5, pady=5)


window.mainloop()