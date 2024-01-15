import tkinter as tk
from tkdragfiles import start_dragfiles_event

root = tk.Tk()
root.title("Drags file to me")
root.geometry("600x200")
lb = tk.Listbox(root, height=500, width=500, selectmode=tk.SINGLE)
lb.pack()

def callback(file_paths):
    for file_path in file_paths:
        lb.insert("end", file_path)

start_dragfiles_event(root,callback)
root.mainloop()
