# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk
from tkinter import ttk
from collections import defaultdict
import utils

# Display Class
class Display(tk.Frame):

    # Constructor - init parent plus set some private attrs
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self.headers = ["dataType|enum/DataType", "dataConvention", "label1|variant/string", "select"]
        self._frame = tk.Frame(self._parent, width = 600, height = 400, borderwidth=5, bg = "blue")
        self._frame.pack(expand = 0, anchor = 'ne', side='top', fill = 'both',padx = 5, pady = 5)
        self._frame_title = tk.Label(self._frame, text = "Display", bg = "white")
        self._frame_title.pack(anchor = "nw")
        self.table_frame = tk.Frame(self._frame, bg = "white" )
        self.table_frame.pack(expand = 1, fill = "both" , anchor = "center")
        self.display_scroll = tk.Scrollbar(self.table_frame, orient= "vertical")
        self.table = ttk.Treeview(self.table_frame, yscrollcommand= self.display_scroll.set ,  columns = self.headers)
        self.table.bind('<Double-1>', self.remove_item )
        self.display_scroll.pack(side="right", fill="y")
        self.display_scroll.config(command=self.table.yview)
        self.rows = defaultdict(list)
        self.count = 0
        self.ids = []
        self.curveNames = []
        
        
        for col in self.headers:
            self.table.heading(col, text=col.title())

        
        self.table.pack(expand = 1, fill = 'both')

    # I wanted to keep most class attributes and methods private. theses get/set methods are for encapulation purposes.
    def get_frame(self):
        return self._frame

    def prepare( self , curve_data , curveName ):
        if curveName in self.curveNames:
            return("Error: Curve Componant already displayed")
        else:
            self.curveNames.append(curveName)
            self.clean_data(curve_data)
            self.insert_data(curveName)
        
        
    def clean_data(self, curve_data):

        group_data = {}

        for group in curve_data:
            data1ds = group["item|UQL/Data1d"]

            group_data["dataType|enum/DataType"] = data1ds["dataType|enum/DataType"]
            group_data["dataConvention"] = data1ds["dataConvention"]
            curve_instrums = data1ds['dataPointList|sequence/object']


            self.traverse_data1ds( group_data, curve_instrums )

    
    
    def traverse_data1ds(self, group_data, curve_instrums):
        for curve_instrum in curve_instrums:
            
            for k in group_data:
                v = group_data[k]
                self.rows[self.count].append(v)
            
            self.rows[self.count].append(curve_instrum["item|UQL/DataPointCurveInstrument"]["label1|variant/string"])
            self.rows[self.count].append(curve_instrum["item|UQL/DataPointCurveInstrument"]["select"])

            self.count +=1

    def insert_data(self, curveName):
        model = self.table.insert('', 'end', text = curveName )
        for index in self.rows:
            values = tuple(self.rows[index])
            self.ids.append( self.table.insert( model , 'end', text = index,  values=values) )

    def remove_item(self, event):
        selected_item = self.table.selection()[0]
        item = self.table.item(selected_item)
        self.curveNames.remove(item["text"])

        self.table.delete(selected_item)
        