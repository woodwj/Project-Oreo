import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import json_manager

# Class for the UI
class UserInterface():
    def __init__(self,parent, main):
        self._main = main
        self._parent = parent
        self._menubar = tk.Menu(self._parent)
        self._parent.config(menu=self._menubar)
        self._fileMenu = tk.Menu(self._menubar)
        self._fileMenu.add_command(label="Open", command=self._onOpen)
        self._fileMenu.add_command(label="Quit", command =self._quitDialogue)
        self._menubar.add_cascade(label="File", menu=self._fileMenu)

    # fucntion for opening file dialogue and calling back to main.
    def _onOpen(self):
        self._fileName =  askopenfilename(title = "Select file")
        self._main._fileOpened(self._fileName)
        
    # function to get a are yoy sure window before quiting
    def _quitDialogue(self):
        if messagebox.askokcancel("ALERT", "Ok to Quit Cancel to Stay"):
            self._parent.quit()
