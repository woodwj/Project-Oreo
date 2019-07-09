# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk

# Blueprints for our 3 window Objects. | Order goes Root -> MainApplication -> Horizplane -> Explorer + (Vertiplane -> Display + Log)
# In this way the horizontal pane has child objects Explorer and the Vertical Pane which itself has child objects Display and Log
# For most of our classes we want them to inherit tk.Frame so they share a common parent/ ancestor class allowing an object. e.g self._parent._parent._label1.set("Hello")
# For our Main Application in particular, this gives a private namespace for all callbacks and private functions

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

#MainApplication Class
class MainApplication(tk.Frame):

    #Constructor - init parent plus set some private attrs
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)        
        self._parent = parent
        self._horizpane = tk.PanedWindow(self._parent)
        self._horizpane.pack(fill = 'both', expand = 1)# init a horizontal plane (orient defs to horizontal) and packs it so it can expand and fill screen both directions
        self._explorer = Explorer(self._horizpane)# create the Explorer frame inside the horizontal pane
        self._horizpane.add(self._explorer.get_frame())# add that plane to the horiz pane
        
        # now using the horizontal plane create the verticle pane
        self._vertipane = tk.PanedWindow(self._horizpane, orient ='vertical')
        self._log = Log(self._vertipane)
        self._display = Display(self._vertipane)
        self._horizpane.add(self._vertipane)
        self._vertipane.add(self._log.get_frame())
        self._vertipane.add(self._display.get_frame())

        
        

# Main
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()