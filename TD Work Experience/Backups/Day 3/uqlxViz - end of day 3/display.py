# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk

# Display Class
class Display(tk.Frame):

    # Constructor - init parent plus set some private attrs
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._frame = tk.Frame(self._parent, width = 600, height = 400, borderwidth=5, bg = "blue")
        self._frame.pack(expand = 1, anchor = 'ne', side='top', fill = 'both',padx = 5, pady = 5)

    # I wanted to keep most class attributes and methods private. theses get/set methods are for encapulation purposes.
    def get_frame(self):
        return self._frame