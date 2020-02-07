from tkinter import * 
import os, sys
from stat import *
  
def lssearch():
    filels.delete(0,END)
    entdir=lsentry.get()
    file_search(entdir)

def file_search(temp):
    user_path = temp

    dirs = os.listdir( user_path )
    dirs.sort()

    for file in dirs:
        print(file)
        print(os.stat(user_path + file).st_size)
        print(os.stat(user_path + file))

win = Tk()
win.title("LS GUI")
win.configure(background="#212121")

Label(win, text="Enter Directory (/ for root): ", bg="#212121", fg="#059c0f").grid(row=0, column=0)

lsentry = Entry(win, width=15, bg="white")
lsentry.grid(row=0, column=2)

Button(win, text="Search", bg="#7a7a7a", fg="Black", command=lssearch).grid(row=0, column=3)


filels = Listbox(win, bg="#212121", fg="#059c0f")
filels.grid(row=3, column=0)
sizels = Listbox(win, bg="#212121", fg="#059c0f")
sizels.grid(row=3, column=5)


mainloop() 
