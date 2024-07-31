from tkinter import END, IntVar, StringVar, Text, Tk, Label, Button, Entry, Spinbox, Scale, Checkbutton, Radiobutton, Listbox

window = Tk()
window.title("First GUI Program")
window.minsize(width=500,height=500)

#Label
my_label = Label(text= "Here is the Label", font= ('Arial', 18, 'bold'))
my_label.pack(side= 'top', pady=10)

def button_click():
    data = text_field.get()
    my_label.config(text=data)

#Button
button = Button(text='Click Me', command=button_click) 
button.pack(pady=10)

#Entry
text_field = Entry(width=30)
text_field.insert(END, string='You need to write something here')
text_field.pack(pady=10)

#TextArea
text_area = Text(height=5, width=20)
text_area.focus()
text_area.insert(END, "Multi line text entry")
text_area.pack()

#SpinBox
def spin_box_used():
    print(spin_box.get())

spin_box = Spinbox(from_=0, to=10, width=5, command=spin_box_used)
spin_box.pack()

#Scale
def scale_used(value):
    print(value)
    
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#CheckBox
def checkbox_used():
    print(check_state.get())
    
check_state = IntVar()
check_button = Checkbutton(text='Is On?', variable=check_state, command=checkbox_used)
check_state.get()
check_button.pack()

#RadioButton
def radio_used():
    print(radio_state.get())
    
radio_state = IntVar()
radio_button1 = Radiobutton(text= 'Option 1', value= 1,variable=radio_state, command= radio_used)
radio_button2 = Radiobutton(text='Option 2', value=2,variable=radio_state, command= radio_used)
radio_button1.pack()
radio_button2.pack()

#Listbox
def listbox_used(event):
    print(list_box.get(list_box.curselection()))

list_box = Listbox(height=4)
fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Watermelon']

for item in fruits:
    list_box.insert(fruits.index(item), item)
    
list_box.bind("<<ListboxSelect>>", listbox_used)
list_box.pack()

window.mainloop()