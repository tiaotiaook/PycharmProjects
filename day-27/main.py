from tkinter import *

window = Tk()

window.title("My First Gui Program")

window.minsize(width = 500,height = 300)
window.config(padx=100,pady=200)



# label

my_label = Label(text = " I Am a Label ",font = ("Arial",24,"bold"))
my_label.config(text="New text")
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)

#button

def button_clicked():

    print("I Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button =Button(text="Click Me",command = button_clicked)
button.grid(column=1,row=1)
# button.pack()

new_button =Button(text="new button",command = button_clicked)
new_button.grid(column=2,row=0)

#

input = Entry(width=10)
# input.pack()
print(input.get())
input.grid(column=2,row=3)



window.mainloop()

