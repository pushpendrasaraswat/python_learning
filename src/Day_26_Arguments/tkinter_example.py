import tkinter


window = tkinter.Tk()
window.title("My FIrst GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    print("I got clicked")
    value= input_entry.get()
    my_label.config(text="I got clicked "+value)

# button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

input_entry = tkinter.Entry(width=15, name="email", show="email")
input_entry.pack()


window.mainloop()