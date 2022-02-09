from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width = 500,height = 300)

label_0 = Label(text="            ",font=("Arial",24,"bold"))
label_0.grid(column=0, row=0)

label_1 = Label(text="is equal to",font=("Arial",24,"bold"))
label_1.grid(column=0, row=1)

label_2 = Label(text="Km",font=("Arial",24,"bold"))
label_2.grid(column=2, row=1)

label_3 = Label(text="Miles",font=("Arial",24,"bold"))
label_3.grid(column=2, row=0)

label_4 = Label(font=("Arial",24,"bold"))
label_4.grid(column=1, row=1)

def button_clicked():
    new_text = int(input.get())*1.609
    label_4.config(text=new_text)


button = Button(text="calculate",command = button_clicked)
button.grid(column=1, row=2)




input = Entry(width = 10)

# print(input.get())
input.grid(column=1,row=0)







window.mainloop()