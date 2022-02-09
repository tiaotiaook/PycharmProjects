from tkinter import *

def button_clicked():
    # print("i got clicked")
    new_text = input.get()
    my_label.config(text =new_text)

window = Tk()
window.title("my first gui program")
window.minsize(width = 500,height = 300)
window.config(padx=100,pady=200)

my_label = Label(text="I am a label",font=("Arial",24,"bold"))
my_label.pack()

my_label["text"]="new text"
# my_label.place(x=100,y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=60,pady=20)

# button



button = Button(text="click me",command = button_clicked)

button.grid(column=1,row=1)

new_button = Button(text="click here",command = button_clicked)

new_button.grid(column=2,row=0)

# entry

input = Entry(width = 10)

print(input.get())
input.grid(column=3,row=2)



window.mainloop()
