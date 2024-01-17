"""----------HEADERS----------"""
import tkinter as tk
import random
import string
w = tk.Tk()

"""----------FUNCTIONS----------"""
def genPwd():
    pwdLen = int(e1.get())
    pwd = ""
    for i in range(pwdLen):
        pwd = pwd + random.choice(string.ascii_letters + string.digits)
    l2.config(text = pwd)

"""----------UI ELEMENTS----------"""
l1 = tk.Label(w, text = "Enter the length of the password: ")
l1.grid(column = 0, row = 0)

e1 = tk.Entry(w)
e1.grid(column = 1, row = 0)

b1 = tk.Button(w, text = "Generate", command = genPwd)
b1.grid(column = 2, row = 0)

l2 = tk.Label(w, text = "")
l2.config(font = ("Courier", 44))
l2.grid(column = 0, row = 1)

"""----------WINDOW OPTIONS----------"""
w.title("Random Password Generator")
w.mainloop()