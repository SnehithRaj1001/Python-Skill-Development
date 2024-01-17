"""----------HEADER AND DECLARATIONS----------"""
import tkinter as tk
w = tk.Tk()
c = 0

"""----------FUNCTIONS----------"""
def op():
    global c
    print(c)
    l1.config(text = c)

def inc():
    global c
    c = c+1
    print(c)
    l1.config(text = c)

def dec():
    global c
    c = c-1
    print(c)
    l1.config(text = c)

def reset():
    global c
    c = 0
    print(c)
    l1.config(text = c)

"""----------UI ELEMENTS----------"""
w.title("Simple Counter")

l1 = tk.Label(w, text = "Hi")
l1.grid(column = 2, row = 0)

b1 = tk.Button(w, text = "Increment", command = inc)
b1.grid(column = 3, row = 1)


b1 = tk.Button(w, text = "Decrement", command = dec)
b1.grid(column = 1, row = 1)

b1 = tk.Button(w, text = "RESET", command = reset)
b1.grid(column = 2, row = 1)

"""----------WINDOW OPTIONS----------"""
w.title("Simple Counter")
w.mainloop()
