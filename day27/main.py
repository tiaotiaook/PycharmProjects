import tkinter
window = tkinter.Tk()
window.title("my first gui program")
window.minsize(width = 500,height = 300)

my_label = tkinter.Label(text="I am a label",font=("Arial",24,"bold"))
my_label.pack(side="left")







window.mainloop()
