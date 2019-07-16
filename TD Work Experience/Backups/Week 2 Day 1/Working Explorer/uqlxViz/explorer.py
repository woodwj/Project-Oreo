# no wildcard import such that all new tcl/ tkk widgets are all accesable by tk
import tkinter as tk
from tkinter import ttk
import json_manager
import utils

def hello():
    print("hello")

# For most of our classes we want them to inherit tk.Frame so they share a common parent/ ancestor class allowing an object. e.g self._parent._parent._label1.set("Hello")
# Explorer Class to select currencies and will talk to the Module that will hande JSON files and pass data to out Display and Output to the Log
# Sub Widgets May include Notebook, filetree ect
# To be Called From the Main Application

class Explorer(tk.Frame):
    
    # Constructor - init parent plus set some private attrs
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._frame = tk.Frame(self._parent, width = 200, height = 600, borderwidth=5, bg = "white")
        self._frame.pack(expand = 0, anchor = 'nw', side='left' ,fill = 'y', padx = 5, pady = 5)
        self._frame_title = tk.Label(self._frame, text = "Explorer")
        self._frame_title.pack(anchor = "nw")
        self.tree = ttk.Treeview(self._frame)
        self.tree["columns"] = ("#1")
        self.tree.heading ('#0', text = 'Componant')
        self.tree.heading ('#1', text = "Value")
        self.tree.pack(expand = 1, fill = 'both')
        self.curveCount = 0
        
       

    
    # I wanted to keep most class attributes and methods private. theses get/set methods are for encapulation purposes.
    def get_frame(self):
        return self._frame

    # to load file then set up treeview          

    def tree_load(self, Tree, Parent, Dictionery, recur_index = 0):
    
        if recur_index == 0:
                CurveID = "Curve_" + str(self.curveCount)
                Tree.insert(Parent, 'end', CurveID, text = CurveID)
                Parent = CurveID


        if isinstance(Dictionery , dict):

            for key in Dictionery :
                value = Dictionery[key]
                
                if isinstance( value , dict):
                    
                    
                    if key == "item|UQL/DataCollection":
                        key = value["dataConvention"]
                    
                        text_key = key
                        key = utils.check_exist(Tree, key)
                        Tree.insert(Parent, 'end', key, text = text_key)

                    else:
                        text_key = key
                        key = utils.check_exist(Tree, key)
                        Tree.insert(Parent, 'end', key, text = text_key)        
                        
                        recur_index +=1
                        self.tree_load( Tree, key, value, recur_index) # These are Currency, fx level
                
                elif isinstance( value , list):
                    text_key = key
                    key = utils.check_exist(Tree, key)
                    if recur_index == 2 and len(key)== 6:
                        dataValue =  value[0][0]['item|UQL/DataPointCurveInstrument']["dataValue"]
                        Tree.insert(Parent, 'end', key, text = text_key, values = (dataValue))
                    else:
                        Tree.insert(Parent, 'end', key, text = text_key)
                        self.tree_load( Tree, key, value , recur_index) # these are the build methods for currency / fx
                
                else: # when reach bottom dict values
                    text_key = key
                    key = utils.check_exist(Tree, key)
                    Tree.insert(Parent, 'end', key, text = text_key , values = (value))
        
        else: # is list recour this way
            for item in Dictionery:
                #recur_index +=1
                self.tree_load( Tree, Parent, item ,recur_index )


    def file_load(self, filename):
        full_dict =  json_manager.read_file(filename)
        #tree_struc = { "modelType": full_dict["modelType"],
        #"baseDate": full_dict["baseDate"],
        #"dataCollection|UQL/DataCollection" : { "fx" : full_dict["dataCollection|UQL/DataCollection"]["fx"] , "currency": full_dict["dataCollection|UQL/DataCollection"]["currency"] },
        #"stateDataCollection|UQL/DataCollection" : "wip" }
        #dataid = (utils.gen_dict_extract(dataCollections, 'dataId') )
        self.curveCount +=1
        self.tree_load( self.tree, '', full_dict )
        


        # treeview populate
        
