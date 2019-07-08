import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.Frame = tk.Frame(parent)

class Explorer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pane = tk.Frame(self.parent, width = 200, height = 600, borderwidth=5, bg = "yellow")
        self.pane.pack(expand = 0, anchor = 'nw', side='left' ,fill = 'both', padx = 5, pady = 5)

class Log(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pane = tk.Frame(self.parent, width = 800, height = 200, borderwidth=5 ,bg = "green")
        self.pane.pack(expand = 0, anchor = 'sw', side='bottom', fill = 'x',padx = 5, pady = 5)

class Display(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pane = tk.Frame(self.parent, width = 600, height = 400, borderwidth=5, bg = "blue")
        self.pane.pack(expand = 1, anchor = 'ne', side='top', fill = 'both',padx = 5, pady = 5)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self.horizpane = tk.PanedWindow(self._parent)
        self.horizpane.pack(fill = 'both', expand = 1)# init a horizontal plane (orient defs to horizontal) and packs it so it can expand and fill screen both directions
        self.explorer = Explorer(self.horizpane)# create the Explorer frame inside the horizontal pane
        self.horizpane.add(self.explorer.pane)# add that plane to the horiz pane
        
        # now using the horizontal plane create the verticle pane
        self.vertipane = tk.PanedWindow(self.horizpane, orient ='vertical')
        self.log = Log(self.vertipane)
        self.display = Display(self.vertipane)
        self.horizpane.add(self.vertipane)
        self.vertipane.add(self.log.pane)
        self.vertipane.add(self.display.pane)

        
        


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()