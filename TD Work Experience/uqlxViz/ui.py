import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import json_manager


class UserInterface():
    def __init__(self, parent):
        self._parent = parent
        self._parent.title("File dialog")
        self._menubar = tk.Menu(self._parent)
        self._parent.config(menu=self._menubar)
        self._fileMenu = tk.Menu(self._menubar)
        self._fileMenu.add_command(label="Open", command=self._onOpen)
        self._fileMenu.add_command(label="Quit", command =self._quitDialogue)
        self._menubar.add_cascade(label="File", menu=self._fileMenu)

    def _onOpen(self):
        self._filename =  askopenfilename(title = "Select file")
        self._parent.main._wlog(f"Opened File {self._filename}")
        json_manager.read_file(self._filename)




    def _quitDialogue(self):
        if messagebox.askokcancel("ALERT", "Ok to Quit Cancel to Stay"):
            self._parent.quit()
