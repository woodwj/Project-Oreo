# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk
import threading
import explorer
import event
import log
import display
import time
import ui

# 3 window Objects. | Order goes Root -> MainApplication -> Horizplane -> Explorer + (Vertiplane -> Display + Log)
# In this way the horizontal pane has child objects Explorer and the Vertical Pane which itself has child objects Display and Log
# For most of our classes we want them to inherit tk.Frame so they share a common parent/ ancestor class allowing an object. e.g self._parent._parent._label1.set("Hello")
# For our Main Application in particular, this gives a private namespace for all callbacks and private functions


#MainApplication Class
class MainApplication(tk.Frame):

    #Constructor - init parent plus set some private attrs
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs,)      
        self._parent = parent
        self._UI = ui.UserInterface(self._parent)
        self._horizpane = tk.PanedWindow(self._parent)
        self._horizpane.pack(fill = 'both', expand = 1)# init a horizontal plane (orient defs to horizontal) and packs it so it can expand and fill screen both directions
        self._explorer = explorer.Explorer(self._horizpane)# create the Explorer frame inside the horizontal pane
        self._horizpane.add(self._explorer.get_frame())# add that plane to the horiz pane
        
        # now using the horizontal plane create the verticle pane
        self._vertipane = tk.PanedWindow(self._horizpane, orient ='vertical')
        self._log = log.Log(self._vertipane)
        self._display = display.Display(self._vertipane)
        self._horizpane.add(self._vertipane)
        self._vertipane.add(self._display.get_frame())
        self._vertipane.add(self._log.get_frame())

    def _wlog(self,msg):
        self._log.emit(msg)


# Main
if __name__ == "__main__":
    root = tk.Tk()
    main = MainApplication(root)
    thread1 = threading.Thread(target=event.event_manager, args=[main])
    thread1.start()
    root.mainloop()
    thread1.join()
    