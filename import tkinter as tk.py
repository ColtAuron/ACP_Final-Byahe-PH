import tkinter as tk
from tkinter import *

#create a window
root = Tk()

greet = tk.Label(
            text = "Hello IT2103",
            foreground = "Blue",
            background = "White",
            width = 10,
            height = 5
)
greet.pack()

Btn_click = Button (root, 
             text = "Exit",
             width = 25,
             height = 5,
             bg = "blue",
             fg = "pink",
             command = exit
)
Btn_click.pack()

label = tk.Label(text = "Name")
Entry = tk.Entry()

label.pack()
Entry.pack()

Frame1 = tk.Frame(master=tk.Button, width=100, height=100, bg="red")
Frame1.pack()

Frame2 = tk.Frame(master=tk.Button, width=50, height=100, bg="yellow")
Frame2.pack()

Frame3 = tk.Frame(master=tk.Button, width=25, height=100, bg="blue")
Frame3.pack()

root.mainloop()