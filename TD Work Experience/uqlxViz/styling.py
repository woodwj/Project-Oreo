from tkinter import ttk


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
