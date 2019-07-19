# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk

import tkinter.scrolledtext as ScrolledText

# Log Class
class Log(tk.Frame,):

    # Constructor - init parent plus set some private attrs
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent

        # create logbox and fill the frame
        self._frame = tk.Frame(self._parent, width = 800, height = 200, borderwidth=5, bg = "white" )
        self._frame_title = tk.Label(self._frame, text = "Output", bg = "white")
        self._frame_title.pack(anchor = "nw")
        self._frame.pack(expand = 0, anchor = 'sw', side='bottom', fill = 'x',padx = 5, pady = 5)
        self._logbox = ScrolledText.ScrolledText(self._frame, state='disabled', )
        self._logbox.configure(font='TkFixedFont',bg = "#d1dbeb")
        self._logbox.pack(expand = 1 , fill = 'both' )

        # start up logo load and write to log
        self._logo = open("media/Logo.txt", "r")
        for self._line in self._logo:
            self._write(self._line)

        self._emit("\n" + "Welcome to uqlxViz v1.0")

    # function to write to the logbox    
    def _emit(self, msg ):
        self._logbox.configure(state='normal')
        self._logbox.insert(tk.END, msg + '\n')
        self._logbox.configure(state='disabled')
        # autoscroll to the bottom
        self._logbox.yview(tk.END)
    
    def _write(self, msg ):
        self._logbox.configure(state='normal')
        self._logbox.insert(tk.END, msg )
        self._logbox.configure(state='disabled')
        # autoscroll to the bottom
        self._logbox.yview(tk.END)




    # I wanted to keep most class attributes and methods private. theses get/set methods are for encapulation purposes.
    def get_frame(self):
        return self._frame
