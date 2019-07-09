# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk

# Log Class
class Log(tk.Frame):

    # Constructor - init parent plus set some private attrs
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._frame = tk.Frame(self._parent, width = 800, height = 200, borderwidth=5 ,bg = "green")
        self._frame.pack(expand = 0, anchor = 'sw', side='bottom', fill = 'x',padx = 5, pady = 5)

    # I wanted to keep most class attributes and methods private. theses get/set methods are for encapulation purposes.
    def get_frame(self):
        return self._frame
