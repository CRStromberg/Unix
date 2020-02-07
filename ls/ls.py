from tkinter import * 
import os, sys
from stat import *
  
def lssearch():
    filels.delete(0, END)
   
    entdir=lsentry.get()
    file_search(entdir)

def file_search(temp):
    user_path = temp

    dirs = os.listdir( user_path )
    dirs.sort()

    for file in dirs:
        print(file)
        filestat = os.stat(user_path + file)
        perms = filemode(filestat.st_mode)
        filesize = filestat.st_size
        info = [file,filesize,perms]
        print(filesize)
        print(perms)
        filels.insert(END, info)
       


win = Tk()
win.title("LS GUI")
win.configure(background="#212121")

Label(win, text="Enter Directory (/ for root): ", bg="#212121", fg="#059c0f", font='bold').grid(row=0, column=0)

lsentry = Entry(win, width=15, bg="white")
lsentry.grid(row=1, column=0)

Button(win, text="Search", bg="#7a7a7a", fg="Black", command=lssearch).grid(row=2, column=0)

Label(win, text="Name, Bytes, Permissions", bg="#212121", fg="#059c0f", width=40, font='bold').grid(row=5, column=0)


filels = Listbox(win, bg="#212121", fg="#059c0f", height=20, width=40)
filels.grid(row=7, column=0)


mainloop() 
