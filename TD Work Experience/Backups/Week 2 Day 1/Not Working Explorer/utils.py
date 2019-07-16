
_validCurrencies = ["USD", "JPY", "EUR", "CAD" ]

def is_currency(x):
    if len(x) != 3:
        return  False
    else:
        return x in _validCurrencies

def is_ccypair(x):
    if len(x) != 6:
        return  False
    else:
        return is_currency(x[0:3]) and is_currency(x[3:6])


def gen_dict_extract(key, var):

    # generalised dictionary extract , find-all-occurrences-of-a-key-in-nested-python-dictionaries-and-lists
    # dcs = list(utils.gen_dict_extract(_dc_key, model_d))

    if hasattr(var,'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result
                        
    def tree_load(self, Tree, Parent, Dictionery):
        if isinstance(Dictionery , dict):

            for key in Dictionery :
                value = Dictionery[key]
                
                if isinstance( value , dict):
                    Tree.insert(Parent, 'end', key, text = key)
                    self.tree_load( Tree, key, value) # These are Currency, fx level
                
                elif isinstance( value , list):
                    Tree.insert(Parent, 'end', key, text = key)
                    self.tree_load( Tree, key, value ) # these are the build methods for currency / fx
                
                else: # when reach bottom dict values
                    Tree.insert(Parent, 'end', key, values = (key, value))
        
        else: # is list recour this way
            for item in Dictionery:
                self.tree_load( Tree, Parent, item )


        if tree_level == 0:
            CurveID = "Curve" + "_" + str(self.curveCount)
            CurveDir = Tree.insert('', 'end', CurveID, text = CurveID )
            
            if isinstance (Dictionery, dict ):
                Parent = CurveDir
                tree_level +=1
                for key , value  in Dictionery.items():
                    if isinstance( value , dict ):
                        Tree.insert(CurveDir, 'end', key, text = key )
                        self.tree_load( Tree, Parent, Dictionery, tree_level)
                    else:
                        Tree.insert(Parent, 'end', key, values = (key, value))

        if tree_level == 1:
            if isinstance( Dictionery, dict):
                for key, value in Dictionery.items():
                    if isinstance( value , dict):
                        Tree.insert(Parent, 'end', key, text = key)
                        self.tree_load( Tree, key, value)
                
            elif isinstance( value , list):
                self.tree_load( Tree, key, value )


    def tree_load(self, Tree, Parent, dictionery, tree_level ):
        if tree_level == 0:
            self.CurveID = "Curve" + "_" + str(self.curveCount)
            self.CurveDir = Tree.insert('', 'end', self.CurveID, text = self.CurveID )
            tree_level += 1
            self.tree_load(Tree, self.CurveDir, dictionery, tree_level)
            return
        
        
        if tree_level == 1:
            if isinstance(dictionery , dict):
                for key , value in dictionery.items():
                    if isinstance(value , dict):
                        tree_level += 1
                        self.tree.insert(Parent, 'end', key, text = key )
                        self.tree_load(Tree, key, value, tree_level)
                    
                    else:
                        self.tree.insert(Parent, 'end', key ,text = key , values = (value))
                        #self.tree_load(Tree, Parent, dictionery, tree_level)
            
            else:
                self.tree.insert(Parent, 'end', key, text = key )
                self.tree_load(Tree, Parent, dictionery, tree_level)
            
        if tree_level == 2:
            if isinstance(dictionery , dict):
                for key , value in dictionery.items():
                    if isinstance(value , dict):
                        tree_level +=1
                        if Tree.exists(key)==False:
                            self.tree.insert(Parent, 'end', key, text = key )
                        self.tree_load(Tree, key, dictionery, tree_level)
                    
                    else:
                        self.tree.insert(Parent, 'end', key ,text = key , values = (value))
                        #self.tree_load(Tree, Parent, dictionery, tree_level)
            else:
                self.tree.insert(Parent, 'end', key, text = key )
                self.tree_load(Tree, Parent, dictionery, tree_level)

        if tree_level == 3:
            if isinstance(dictionery , dict):
                for key , value in dictionery.items():
                    if isinstance(value , dict):
                        tree_level +=1
                        if Tree.exists(key)==False:
                            self.tree.insert(Parent, 'end', key, text = key )
                        self.tree_load(Tree, key, dictionery, tree_level)
                    
                    else:
                        self.tree.insert(Parent, 'end', key ,text = key , values = (value))
                        #self.tree_load(Tree, Parent, dictionery, tree_level)
            else:
                self.tree.insert(Parent, 'end', key, text = key )
                self.tree_load(Tree, Parent, dictionery, tree_level)



def check_exist(tree, key):
    if tree.exists(key)==False:
        return(key)
    else:
        key = key + "1"
        return(check_exist(tree, key))