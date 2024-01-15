<div align="center">
    <img src="https://raw.githubusercontent.com/nicehero/tkdragfiles/main/show.gif"/>
</div>

<div align="center">
    
[![PyPI](https://img.shields.io/pypi/v/tkdragfiles)](https://pypi.org/project/tkdragfiles/)

</div>

# Easy Drag Files and Drop to Tkinter

Only for windows

## Installation
```shell
pip3 install tkdragfiles
pip3 install async_tkinter_loop #if u need asyncio
```
## Easy to use 
```python
#for normal tk
import tkinter as tk
from tkdragfiles import start_dragfiles_event

root = tk.Tk()
root.geometry("600x200")
lb = tk.Listbox(root, height=500, width=500, selectmode=tk.SINGLE)
lb.pack()

def callback(file_paths):
    for file_path in file_paths:
        lb.insert("end", file_path)

start_dragfiles_event(root,callback)
root.mainloop()
```
```python
#for asyncio tk
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
```

## References
