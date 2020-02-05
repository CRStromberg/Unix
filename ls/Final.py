#ls for Unix
from tkinter import *


def searchls():
    Label (win, text="It Worked!", bg="#212121", fg="#1a8a4a").grid(row=5, column=5)

win = Tk()
win.title("LS")
win.config(background = "#212121")

Label (win, text="Enter Directory:", bg="#212121",fg="#1a8a4a").grid(row=0, column=0)

lsentry = Entry(win, width=15, bg="white")
lsentry.grid(row=0, column=1)

Button(win, text="Search", command=searchls).grid(row=1, column=0)

win.mainloop()