# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk
from tkinter import ttk
import json_manager
import utils


# For most of our classes we want them to inherit tk.Frame so they share a common parent/ ancestor class allowing an object. e.g self._parent._parent._label1.set("Hello")
# Explorer Class to select currencies and will talk to the Module that will hande JSON files and pass data to out Display and Output to the Log
# Sub Widgets May include Notebook, filetree ect
# To be Called From the Main Application

class Explorer(tk.Frame):
    
    # Constructor - init parent plus set some private attrs
    def __init__(self, parent, display_callback, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.display_callback = display_callback
        self._parent = parent

        self._frame = tk.Frame(self._parent, borderwidth=5, bg = "#323f54")
        self._frame.pack(expand = 0, anchor = 'nw', side='left' ,fill = 'y', padx = 5, pady = 5)
        
        self._frame_title = tk.Label(self._frame, text = "Explorer", bg = "#4287f5", fg = 'white')
        self._frame_title.pack(anchor = "nw")
        
        self.tree = ttk.Treeview(self._frame, style= "Custom.Treeview" )
        self.tree["columns"] = ("#1")
        self.tree.heading ('#0', text = 'Component')
        self.tree.heading ('#1', text = "Value")
        self.tree.pack(expand = 1, fill = 'both')
        self.tree.bind('<Double-1>', self.selectItem)
        
        self.currency_curves = {}
        self.curveIDs = []
        
        # styling oddly this is global maybe. not sure how this part of tk works
        style = ttk.Style()
        style.element_create("Custom.Treeheading.border", "from", "default")
        style.layout("Custom.Treeview.Heading", [
        ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
        ("Custom.Treeheading.border", {'sticky':'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky':'nswe', 'children': [
        ("Custom.Treeheading.image", {'side':'top', 'sticky':'nswe'}),
        ("Custom.Treeheading.text", {'sticky':'nswe'})
                ]})
            ]}),
        ])
        style.configure("Custom.Treeview.Heading",
        background="#4287f5", foreground="white", relief="flat")
        style.map("Custom.Treeview.Heading",
        relief=[('active','groove'),('pressed','sunken')]) 
       

    
    # I wanted to keep most class attributes and methods private. theses get/set methods are for encapulation purposes.
    def get_frame(self):
        return self._frame

    def file_load(self, filename,):
        
        self.currency_curves = {}
        full_dict =  json_manager.read_file(filename)
        self.CurveID = utils.extract_file_name(filename)
        if self.CurveID in self.curveIDs:
            return f"Error duplicate curve: {self.CurveID}"
        else:
            self.curveIDs.append(self.CurveID)
            self.tree_load( self.tree, '', full_dict , 0)
        

    # tree key checkser and inserter

             
    # to load file then set up treeview 
    def tree_load(self, Tree, Parent, Dictionery, recur_index = 0):
        
        # When adding a new curve
        if recur_index == 0:
                Parent = Tree.insert(Parent, 'end', text = self.CurveID)

        # if pased a dictionary
        if isinstance(Dictionery , dict):

            # loop through dictionary. key, value will goo too deep so only keys
            for key in Dictionery :
                value = Dictionery[key]

                # if the value is a dict and another level must be traversed    
                if isinstance( value , dict):
                    
                    # hard coding to cut off at the curve data convenction at currencies
                    if key == "item|UQL/DataCollection":
                        name = self.tree.item(Parent)['text']
                        if utils.is_currency(name):
                            if name not in self.currency_curves:
                                self.currency_curves[name] = {}
                        else:
                            self.currency_curves[name][key] = value["dataConvention"]

                        key = value["dataConvention"]
                        self.currency_curves[name][key] = value['dataList|sequence/object']
                        Parent = self.tree.insert(Parent, 'end' , text = key)
                    
                    # Other wise if not at that key then insert and go to the next level
                    else:

                        key =  self.tree.insert(Parent,'end' , text = key)
                        recur_index +=1
                        self.tree_load( Tree, key, value, recur_index)
                
                # if the value of the dict is a list then check if at currency pair level
                elif isinstance( value , list):

                    text_key = key
                    
                    
                    #if at currency pair level insert the key and the value of the fx
                    if recur_index == 2 and len(key)== 6:
                        
                        dataValue =  value[0][0]['item|UQL/DataPointCurveInstrument']["dataValue"]
                        Tree.insert(Parent, 'end', text = text_key, values = (dataValue))
                    
                    # if not at that level just insert and recour
                    else:
                        key = Tree.insert(Parent, 'end', text = text_key)
                        self.tree_load( Tree, key, value , recur_index)
                
                # when dict values are data then insert with the value
                else:
                    key = self.tree.insert( Parent, 'end' ,text = key ,values = value)
        
        # otherwise if the value passed as dict is a list loop through but dont insert
        else:
            for item in Dictionery:
                self.tree_load( Tree, Parent, item ,recur_index )

    def selectItem(self, event ):
        # checks that parents parent is curencies and if so loads display
        item_iid = self.tree.selection()[0]
        parent_iid = self.tree.parent(item_iid)
        name_parent = self.tree.item(parent_iid)['text']
        name_item = self.tree.item(item_iid)['text']
        if utils.is_currency(name_parent):
            Curve_componants = (self.currency_curves[name_parent][name_item])
            self.display_callback(Curve_componants, name_item)

        
        