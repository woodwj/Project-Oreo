# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk

def hello():
    print("hello")

# For most of our classes we want them to inherit tk.Frame so they share a common parent/ ancestor class allowing an object. e.g self._parent._parent._label1.set("Hello")
# Explorer Class to select currencies and will talk to the Module that will hande JSON files and pass data to out Display and Output to the Log
# Sub Widgets May include Notebook, filetree ect
# To be Called From the Main Application

class Explorer(tk.Frame):
    
    # Constructor - init parent plus set some private attrs
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._frame = tk.Frame(self._parent, width = 200, height = 600, borderwidth=5, bg = "yellow")
        self._frame.pack(expand = 0, anchor = 'nw', side='left' ,fill = 'y', padx = 5, pady = 5)
    
    # I wanted to keep most class attributes and methods private. theses get/set methods are for encapulation purposes.
    def get_frame(self):
        return self._frame