# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk
import utils
import tkinter.scrolledtext as ScrolledText

# Log Class
class Log(tk.Frame,):

    # Constructor - init parent plus set some private attrs
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent

        # create logbox and fill the frame
        self._frame = tk.Frame(self._parent, borderwidth=5, bg = "#323f54" )
        self._frame.pack(expand = 0, anchor = 'sw', side='bottom', fill = 'x',padx = 5, pady = 5)

        # frame title
        self._frame_title = tk.Label(self._frame, text = "Output", bg = "#4287f5", fg = 'white')
        self._frame_title.pack(anchor = "nw")

        # log text box
        self._logbox = ScrolledText.ScrolledText(self._frame, state='disabled' )
        self._logbox.configure(font='TkFixedFont',bg = "#8e96a3")
        self._logbox.pack(expand = 1 , anchor = "nw", fill = "x" )

        # container frame for input line
        self._input_frame =tk.Frame(self._frame, borderwidth = 5, height = 200, bg = "#323f54")
        self._input_frame.pack(fill = "both", anchor = "sw", expand = 0)

        # title for input line
        self._input_title = tk.Label(self._input_frame, text = "Command", bg = "#4287f5", fg = 'white')
        self._input_title.pack(anchor = "nw", fill = "none", expand = 0)

        # entry widget for command
        self._input = tk.Entry(self._input_frame, borderwidth = 5, bg = "white")
        self._input.pack(fill = "x", expand = 0, anchor = "nw")
        self._input.bind("<Return>", self._command)


        # start up logo load and write to log
        self._logo("media/Logo.txt")

    #logo function that runs at start + in multicolour with command line
    def _logo(self , filename, colour = "white"):
        logo = open(filename, "r")
        for self._line in logo:
            if colour != "white":
                colour = utils.random_colour()
            self._logbox.configure(state='normal')
            self._logbox.insert(tk.END, self._line[:-1] + "\n", colour )
            self._logbox.tag_configure(colour, foreground = colour, font = ("Courier",8, "bold"))
            self._logbox.configure(state='disabled')
            # autoscroll to the bottom
            
        self._emit("\n" + "Welcome to uqlxViz v1.0", "white")

    # function to write to the logbox    
    def _emit(self, msg, colour = "black" ):
        self._logbox.configure(state='normal')
        self._logbox.insert(tk.END, msg + '\n', colour )
        self._logbox.tag_configure(colour, foreground = colour)
        self._logbox.configure(state='disabled')
        # autoscroll to the bottom
        self._logbox.yview(tk.END)

    # callback for entry box on return key
    def _command(self, event):
        inp = self._input.get()
        if inp == "- logo":
            self._logo("media/Logo.txt", "")
        self._input.delete(0, 'end')





    # I wanted to keep most class attributes and methods private. theses get/set methods are for encapulation purposes.
    def get_frame(self):
        return self._frame
