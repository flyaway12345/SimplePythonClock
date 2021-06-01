from tkinter import * 
from tkinter.ttk import * 

from time import strftime

root = Tk()
root.title("Clock")

def time():
    timeFormat = strftime('%I:%M:%S %p')
    #clockDisplayLable
    label.config(text=timeFormat)
    label.after(1000, time)

label = Label(root, font=("Arial"), background='black', foreground='white')
label.pack(anchor='center')

time()

mainloop()