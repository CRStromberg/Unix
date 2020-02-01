import tkinter as tk
#import os
from pathlib import Path
import glob

win = tk.Tk()
win.title("LS GUI")
win.geometry('475x275')
win.configure(bg='#292929')

types = ('*.*')

p = Path('/home/chris')
filels = p.iterdir()

files_grabbed = []
for files in types:
    files_grabbed.extend(glob.glob(files))

#filels = os.listdir('/')

lbox = tk.Listbox(win, width=60, height=40, bg='#292929', fg='#dfdfdf')
lbox.pack()

for item in files_grabbed:
    lbox.insert(tk.END, item)
 
win.mainloop()