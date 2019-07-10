# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk
import logging
import tkinter.scrolledtext as ScrolledText

# Log Class
class Log(tk.Frame,):

    # Constructor - init parent plus set some private attrs
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._frame = tk.Frame(self._parent, width = 800, height = 200, borderwidth=5 ,bg = "#d1dbeb")
        self._frame.pack(expand = 0, anchor = 'sw', side='bottom', fill = 'x',padx = 5, pady = 5)
        self._logbox = ScrolledText.ScrolledText(self._frame, state='disabled')
        self._logbox.configure(font='TkFixedFont')
        self._logbox.pack(expand = 1 , fill = 'both' )
        

    
    def emit(self, record):
        msg = record
        def append():
            self._logbox.configure(state='normal')
            self._logbox.insert(tk.END, msg + '\n')
            self._logbox.configure(state='disabled')
            # Autoscroll to the bottom
            self._logbox.yview(tk.END)
        # This is necessary because we can't modify the Text from other threads
        self._logbox.after(0, append)


    # I wanted to keep most class attributes and methods private. theses get/set methods are for encapulation purposes.
    def get_frame(self):
        return self._frame
