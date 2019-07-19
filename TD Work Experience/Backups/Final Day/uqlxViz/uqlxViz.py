# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk
import explorer
import log
import display
import ui

# 3 window Objects. | RootOrder goes Root -> UI + ( MainApplication -> Horizplane -> Explorer + (Vertiplane -> Display + Log) )
# In this way the horizontal pane has child objects Explorer and the Vertical Pane which itself has child objects Display and Log
# It is ok to have these as child objects even though they are also child objects of the MainApp aas we have no use for the panes futher than just getting them to slide
# For most of our widget classes we want them to inherit tk.Frame so they share a common parent/ ancestor class allowing an object. e.g self._parent._parent._label1.set("Hello")
# For our Main Application in particular, this gives a private namespace for all callbacks and private functions


#MainApplication Class
class MainApplication(tk.Frame):

    #Constructor - init parent plus set some private attrs
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs,)      
        self._parent = parent

        #create UI object
        self._UI = ui.UserInterface(self._parent, self)

        # init a horizontal plane (orient defs to horizontal) and packs it so it can expand and fill screen both directions
        self._horizpane = tk.PanedWindow(self._parent)
        self._horizpane.pack(fill = 'both', expand = 1)
        
        # create the Explorer frame with and add to the horizontal pane 
        self._explorer = explorer.Explorer(self._horizpane, self.setup_display)
        self._horizpane.add(self._explorer.get_frame())
        
        # now using the horizontal plane create the verticle pane
        self._vertipane = tk.PanedWindow(self._horizpane, orient ='vertical')

        # create log object with vertical pane
        self._log = log.Log(self._vertipane)

        # create the display object with the veritcal pane
        self._display = display.Display(self._vertipane)

        # adding the vertical plane to the horizontal
        self._horizpane.add(self._vertipane)

        # adding the display and log to the display
        self._vertipane.add(self._display.get_frame())
        self._vertipane.add(self._log.get_frame())

        # window metadata
        self._parent.title("uqlxViz")

    # a write log procedure that just makes it acessable as a method of main not of the object
    def _wlog(self,msg):
        self._log._emit(msg)

    # function for opening a file which will open the tree view in explorer frame
    def _fileOpened(self, filename):
        self._wlog(f"Opened File {filename}")

        self._wlog("File processing ...")
        # calls exploere object funciton which will delegate
        self._explorer.file_load(filename)
        # when call stack return back to our main file. write to log file has been loaded
        self._wlog("File loaded to Explorer.")


    def setup_display(self, currency_curve, curve_name):
        self._wlog("Displaying curve componant...")
        return_msg = self._display.prepare( currency_curve, curve_name )
        if return_msg:
            self._wlog( return_msg )
        else:
            self._wlog("Componant displayed succesfully.")


# Main
if __name__ == "__main__":
    root = tk.Tk()
    main = MainApplication(root)
    root.mainloop()
   