import tkinter as tk 
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=((".exe", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
#openFile.pack()

<<<<<<< HEAD
#runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42")
#runApps.pack()
command = list_files
=======
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()
>>>>>>> 04636a09327afa726d7e2b287b8ccd5c12dc0649

root.mainloop()