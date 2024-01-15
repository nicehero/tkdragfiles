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

from async_tkinter_loop import async_handler, async_mainloop,get_event_loop,main_loop

loop = get_event_loop()
loop.run_until_complete(main_loop(root))
