import tkinter as tk
import os
from pathlib import Path
import glob
import sys

def searchdir():
    for item in filels:
        lbox.insert(tk.END, item)

p = Path(useren)

filels = os.listdir(p)

win = tk.Tk()
win.title("LS GUI")
win.geometry('475x275')
win.configure(bg='#292929')

userin = tk.Label(win, text="Directory")
userin.pack()
useren = tk.Entry(win)
useren.pack()

search_dir = tk.Button(win, text="Search", command=searchdir)
search_dir.pack()

lbox = tk.Listbox(win, width=60, height=40, bg='#292929', fg='#dfdfdf')
lbox.pack()


win.mainloop()