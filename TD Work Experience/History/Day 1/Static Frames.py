import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.Frame = tk.Frame(parent)

class Explorer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pane = tk.PanedWindow(self.parent, width = 200, height = 600, borderwidth=5, bg = "yellow").pack(expand = 0, anchor = 'nw', side='left' ,fill = 'both', padx = 5, pady = 5)

class Log(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pane = tk.PanedWindow(self.parent, width = 800, height = 200, borderwidth=5 ,bg = "green", orient = 'vertical').pack(expand = 0, anchor = 'sw', side='bottom', fill = 'x',padx = 5, pady = 5)

class Display(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pane = tk.PanedWindow(self.parent, width = 600, height = 400, borderwidth=5, bg = "blue", orient = 'horizontal').pack(expand = 1, anchor = 'ne', side='top', fill = 'both',padx = 5, pady = 5)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.log = Log(self.parent)
        self.Explorer = Explorer(self.parent)
        self.Display = Display(self.parent)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()